from werkzeug.security import generate_password_hash

HTTPBASICAUTH_USERS = {
    "{HTTP auth ID}": generate_password_hash("{HTTP auth password}"),
}

SLACK_INFO = {
    "url": "{your slack hook url}",
    "channel": "{your slack channel name}",
    "bot_name": "Uptime Check",
    "bot_emoji": "white_check_mark",
}

SEND_MESSAGE_INTERVAL = 30
