* {
  box-sizing: border-box;
}

:root {
  --bg: #0d1117;
  --panel: #161b22;
  --text: #c9d1d9;
  --muted: #8b949e;
  --link: #58a6ff;
  --accent: #238636;
  --border: #30363d;
}

html,
body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--text);
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.6;
}

a {
  color: var(--link);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

header {
  border-bottom: 1px solid var(--border);
  background: rgba(13, 17, 23, 0.95);
  position: sticky;
  top: 0;
  backdrop-filter: blur(6px);
}

.container {
  width: min(1040px, 92vw);
  margin: 0 auto;
}