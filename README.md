# McBot
A discord bot to control multicraft minecraft servers.


## config
config.yml
```yml
# Discord bot token
token: "DISCORD_BOT_TOKEN"

api-user: "ENTER_PANEL_EMAIL"
api-key: "ENTER_API_KEY"

# Command prefix
prefix: "!"

servers:
    # name: server_id
    survival: 153701

permissions:
    users:
        "000000000000000000": # user id
            - start
            - stop
            - command
            - status
            - restart
            - help
            - maintenance
    roles:
        "000000000000000000": # role id
            - status

# If you add any channel IDs here, then the bot will only work in this channel
channel_whitelist: []

emojis:
    error: "❌"
    apiError: "⚠️"
    online: "🟢"
    offline: "🔴"
    success: "✅"

scripts:
    maintenance:
        # Example script for server survival
        - command survival maintenance on
```
