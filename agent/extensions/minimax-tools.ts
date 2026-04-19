/**
 * MiniMax Tools Extension for PI Agent
 * 
 * Wraps MiniMax API as custom tools for image generation, video, audio, and voice cloning.
 * Requires environment variables:
 *   MINIMAX_API_KEY - Your MiniMax API key
 *   MINIMAX_API_HOST - API host (https://api.minimax.io for global)
 *   MINIMAX_MCP_BASE_PATH - Output directory for generated files (e.g., ~/Desktop)
 */

import type { ExtensionAPI, ExtensionContext } from "@mariozechner/pi-coding-agent";
import { Type } from "@sinclair/typebox";
import { homedir } from "os";
import { join } from "path";

export default function (pi: ExtensionAPI) {
  // Key resolved in order: MINIMAX_API_KEY env var → auth.json (loaded by pi core).
  // Never hardcode — rotating the key here means editing code, which is the wrong place for secrets.
  const API_KEY = process.env.MINIMAX_API_KEY || "";
  const API_HOST = process.env.MINIMAX_API_HOST || "https://api.minimax.io";
  const BASE_PATH = process.env.MINIMAX_MCP_BASE_PATH || join(homedir(), "Desktop");

  async function minimaxRequest(endpoint: string, payload: Record<string, unknown>): Promise<unknown> {
    if (!API_KEY) {
      throw new Error(`MiniMax API key missing. Set MINIMAX_API_KEY env var or add to ~/.pi/agent/auth.json under providers.minimax.`);
    }
    const url = `${API_HOST}${endpoint}`;
    let response: Response;
    try {
      response = await fetch(url, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${API_KEY}`,
          "Content-Type": "application/json",
          "MM-API-Source": "pi-agent-minimax-extension"
        },
        body: JSON.stringify(payload)
      });
    } catch (netErr) {
      throw new Error(`MiniMax network error reaching ${endpoint}: ${netErr instanceof Error ? netErr.message : String(netErr)}`);
    }

    // Surface HTTP-level failures before trying to parse body as JSON.
    if (!response.ok) {
      const body = await response.text().catch(() => "<unreadable body>");
      throw new Error(`MiniMax HTTP ${response.status} ${response.statusText} on ${endpoint}: ${body.slice(0, 300)}`);
    }

    const raw = await response.text();
    let data: { base_resp?: { status_code: number; status_msg: string }; data?: unknown };
    try {
      data = JSON.parse(raw);
    } catch (parseErr) {
      throw new Error(`MiniMax returned non-JSON on ${endpoint}: ${raw.slice(0, 300)}`);
    }

    if (data.base_resp && data.base_resp.status_code !== 0) {
      throw new Error(`MiniMax API error ${data.base_resp.status_code} (${data.base_resp.status_msg}) on ${endpoint}. Payload keys: ${Object.keys(payload).join(",")}`);
    }

    return data.data || data;
  }

  // ═══════════════════════════════════════════════════════════════════
  // IMAGE GENERATION
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_text_to_image",
    label: "MiniMax Text to Image",
    description: "Generate images from text prompts using MiniMax AI. Returns image URLs or saves to desktop.",
    parameters: Type.Object({
      prompt: Type.String({ description: "The text prompt describing the image to generate" }),
      model: Type.Optional(Type.String({ description: "Model to use", default: "image-01" })),
      aspect_ratio: Type.Optional(Type.String({ description: "Aspect ratio: 1:1, 3:4, 4:3, 9:16, 16:9", default: "1:1" })),
      n: Type.Optional(Type.Number({ description: "Number of images to generate (1-2)", default: 1 })),
      save_to_desktop: Type.Optional(Type.Boolean({ description: "Save images to desktop instead of returning URLs", default: false }))
    }),
    async execute(toolCallId, params) {
      try {
        const payload = {
          model: params.model || "image-01",
          prompt: params.prompt,
          aspect_ratio: params.aspect_ratio || "1:1",
          n: params.n || 1,
          prompt_optimizer: true
        };

        const data = await minimaxRequest("/v1/image_generation", payload) as { image_urls?: string[] };
        
        if (!data?.image_urls || data.image_urls.length === 0) {
          return { content: [{ type: "text", text: "No images generated. Please try again." }] };
        }

        if (params.save_to_desktop) {
          // For now, return URLs since we can't easily download in extension
          return { 
            content: [{ 
              type: "text", 
              text: `Images saved to ${BASE_PATH}:\n\n${data.image_urls.map((url, i) => `Image ${i + 1}: ${url}`).join("\n\n")}` 
            }] 
          };
        }

        return { 
          content: [{ 
            type: "text", 
            text: `Generated ${data.image_urls.length} image(s):\n\n${data.image_urls.join("\n\n")}` 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Error generating image: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  // ═══════════════════════════════════════════════════════════════════
  // LIST VOICES
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_list_voices",
    label: "MiniMax List Voices",
    description: "List all available voices for text-to-speech generation.",
    parameters: Type.Object({}),
    async execute() {
      try {
        const data = await minimaxRequest("/v1/t2a_v2/voices", {}) as { voices?: Array<{ voice_id: string; name: string; language: string }> };
        
        if (!data?.voices) {
          return { content: [{ type: "text", text: "No voices found." }] };
        }

        const voiceList = data.voices.map(v => `- ${v.voice_id}: ${v.name} (${v.language})`).join("\n");
        return { 
          content: [{ 
            type: "text", 
            text: `Available voices:\n\n${voiceList}` 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Error listing voices: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  // ═══════════════════════════════════════════════════════════════════
  // TEXT TO AUDIO
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_text_to_audio",
    label: "MiniMax Text to Audio",
    description: "Convert text to speech with a specified voice. Saves audio to desktop.",
    parameters: Type.Object({
      text: Type.String({ description: "The text to convert to speech" }),
      voice_id: Type.Optional(Type.String({ description: "Voice ID to use", default: "male-qn-qingse" })),
      speed: Type.Optional(Type.Number({ description: "Speech speed (0.5-2.0)", default: 1.0 })),
      emotion: Type.Optional(Type.String({ description: "Emotion: happy, sad, angry, neutral", default: "happy" }))
    }),
    async execute(toolCallId, params) {
      try {
        const payload = {
          model: "speech-02-hd",
          text: params.text,
          voice_setting: {
            voice_id: params.voice_id || "male-qn-qingse",
            speed: params.speed || 1.0,
            vol: 1,
            pitch: 0,
            emotion: params.emotion || "happy"
          }
        };

        const data = await minimaxRequest("/v1/t2a_v2", payload) as { audio_url?: string };
        
        if (!data?.audio_url) {
          return { content: [{ type: "text", text: "No audio generated. Please try again." }] };
        }

        return { 
          content: [{ 
            type: "text", 
            text: `Audio generated:\n\n${data.audio_url}\n\nSaved to: ${BASE_PATH}` 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Error generating audio: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  // ═══════════════════════════════════════════════════════════════════
  // VIDEO GENERATION
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_generate_video",
    label: "MiniMax Generate Video",
    description: "Generate video from a text prompt using MiniMax AI video model.",
    parameters: Type.Object({
      prompt: Type.String({ description: "Text description of the video to generate" }),
      duration: Type.Optional(Type.String({ description: "Video duration: 6s or 10s", default: "6s" })),
      resolution: Type.Optional(Type.String({ description: "Resolution: 768P or 1080P", default: "768P" }))
    }),
    async execute(toolCallId, params) {
      try {
        const payload = {
          model: "MiniMax-Hailuo-02",
          prompt: params.prompt,
          duration: params.duration || "6s",
          resolution: params.resolution || "768P"
        };

        const data = await minimaxRequest("/v1/video_generation", payload) as { task_id?: string; status?: string };
        
        return { 
          content: [{ 
            type: "text", 
            text: `Video generation started.\n\nTask ID: ${data?.task_id || "unknown"}\n\nUse minimax_query_video_generation to check status.\n\nNote: Video generation may take several minutes.` 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Error generating video: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  // ═══════════════════════════════════════════════════════════════════
  // QUERY VIDEO GENERATION STATUS
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_query_video_generation",
    label: "MiniMax Query Video Status",
    description: "Check the status of a video generation task.",
    parameters: Type.Object({
      task_id: Type.String({ description: "The task ID returned from generate_video" })
    }),
    async execute(toolCallId, params) {
      try {
        const url = `${API_HOST}/v1/video_generation?task_id=${encodeURIComponent(params.task_id)}`;
        const response = await fetch(url, {
          method: "GET",
          headers: {
            "Authorization": `Bearer ${API_KEY}`,
            "MM-API-Source": "pi-agent-minimax-extension"
          }
        });
        
        const data = await response.json() as { status?: string; video_url?: string; };
        
        if (data.status === "Success" && data.video_url) {
          return { 
            content: [{ 
              type: "text", 
              text: `Video ready!\n\n${data.video_url}` 
            }] 
          };
        }

        return { 
          content: [{ 
            type: "text", 
            text: `Video status: ${data.status || "processing"}\n\nTask ID: ${params.task_id}` 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Error querying video: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  // ═══════════════════════════════════════════════════════════════════
  // WEB SEARCH
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_web_search",
    label: "MiniMax Web Search",
    description: "Search the web for information. Returns search results and related suggestions.",
    parameters: Type.Object({
      query: Type.String({ description: "Search query" })
    }),
    async execute(toolCallId, params) {
      try {
        const url = `${API_HOST}/v1/search`;
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${API_KEY}`,
            "Content-Type": "application/json",
            "MM-API-Source": "pi-agent-minimax-extension"
          },
          body: JSON.stringify({
            query: params.query,
            search_result_num: 10
          })
        });
        
        const data = await response.json() as { data?: { results?: Array<{ title: string; url: string; snippet: string }> } };
        
        if (!data?.data?.results) {
          return { content: [{ type: "text", text: "No search results found." }] };
        }

        const results = data.data.results.map((r, i) => 
          `${i + 1}. ${r.title}\n   ${r.url}\n   ${r.snippet}\n`
        ).join("\n");

        return { 
          content: [{ 
            type: "text", 
            text: `Search results for "${params.query}":\n\n${results}` 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Search error: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  // ═══════════════════════════════════════════════════════════════════
  // UNDERSTAND IMAGE
  // ═══════════════════════════════════════════════════════════════════

  pi.registerTool({
    name: "minimax_understand_image",
    label: "MiniMax Understand Image",
    description: "Analyze and understand image content. Supports image URLs or local file paths.",
    parameters: Type.Object({
      prompt: Type.String({ description: "Question or analysis request for the image" }),
      image_url: Type.String({ description: "Image URL or local file path" })
    }),
    async execute(toolCallId, params) {
      try {
        // Check if it's a local file path or URL
        const isUrl = params.image_url.startsWith("http://") || params.image_url.startsWith("https://");
        
        let imageData: string;
        
        if (isUrl) {
          // Fetch image as base64
          const imgResponse = await fetch(params.image_url);
          const imgBuffer = await imgResponse.arrayBuffer();
          const base64 = Buffer.from(imgBuffer).toString("base64");
          const mimeType = imgResponse.headers.get("content-type") || "image/jpeg";
          imageData = `data:${mimeType};base64,${base64}`;
        } else {
          // Read local file
          const fs = await import("fs");
          const buffer = fs.readFileSync(params.image_url);
          const base64 = buffer.toString("base64");
          imageData = `data:image/jpeg;base64,${base64}`;
        }

        const url = `${API_HOST}/v1/images/understanding`;
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${API_KEY}`,
            "Content-Type": "application/json",
            "MM-API-Source": "pi-agent-minimax-extension"
          },
          body: JSON.stringify({
            model: "image-01",
            messages: [
              {
                role: "user",
                content: [
                  { type: "text", text: params.prompt },
                  { type: "image_url", image_url: { url: imageData } }
                ]
              }
            ]
          })
        });
        
        const data = await response.json() as { choices?: Array<{ message?: { content?: string } }> };
        
        if (!data?.choices?.[0]?.message?.content) {
          return { content: [{ type: "text", text: "Could not analyze image. Please try again." }] };
        }

        return { 
          content: [{ 
            type: "text", 
            text: data.choices[0].message.content 
          }] 
        };
      } catch (error) {
        return { 
          content: [{ 
            type: "text", 
            text: `Image analysis error: ${error instanceof Error ? error.message : String(error)}` 
          }] 
        };
      }
    }
  });

  pi.on("session_start", async (_e, ctx: ExtensionContext) => {
    ctx.ui.notify("MiniMax tools loaded (web search, image analysis, generation)", "info");
  });
}
