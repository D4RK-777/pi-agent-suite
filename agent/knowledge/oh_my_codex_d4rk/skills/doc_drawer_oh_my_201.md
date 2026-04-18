abled": false
  }
}
```

## State Management

Use `omx_state` MCP tools for ecomode lifecycle state.

- **On activation**:
  `state_write({mode: "ecomode", active: true})`
- **On deactivation/completion**:
  `state_write({mode: "ecomode", active: false})`
- **On cancellation/cleanup**:
  run `$cancel` (which should call `state_clear(mode="ecomode")`)