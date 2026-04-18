igured (OMX present)` };
      }
      return {
        name: 'MCP Servers',
        status: 'warn',
        message: `${mcpCount} servers but no OMX servers yet (expected before first setup; run "omx setup --force" once)`,
      };
    }
    return { name: 'MCP Servers', status: 'warn', message: 'no MCP servers configured' };
  } catch {
    return { name: 'MCP Servers', status: 'fail', message: 'cannot read config.toml' };
  }
}