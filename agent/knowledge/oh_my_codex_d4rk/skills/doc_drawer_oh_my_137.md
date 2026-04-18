session-idle"] = {enabled: true} |
   .notifications.events["ask-user-question"] = {enabled: true} |
   .notifications.events["session-stop"] = {enabled: true} |
   .notifications.events["session-end"] = {enabled: true} |
   .notifications.openclaw = (.notifications.openclaw // {}) |
   .notifications.openclaw.enabled = true |
   .notifications.openclaw.gateways = (.notifications.openclaw.gateways // {}) |
   .notifications.openclaw.gateways["local"] = {
     type: "command",
     command: $command,
     timeout: 120000
   } |
   .notifications.openclaw.hooks = (.notifications.openclaw.hooks // {}) |
   .notifications.openclaw.hooks["session-start"] = {
     enabled: true,
     gateway: "local",