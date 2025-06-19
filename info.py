import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', '')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
BOT_USERNAME = environ.get("BOT_USERNAME", '') # without @

# Admins, Channels & Users
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '')) # admin your channel in stream 
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '')) # admin your channel in users log 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
OWNER_USERNAME = environ.get("OWNER_USERNAME", '') # without @

# pics information
PICS = environ.get('PICS', '')

# channel link information
CHANNEL = environ.get('CHANNEL', '')
SUPPORT = environ.get('SUPPORT', '')

# file limit information
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", False)
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", "600"))
MAX_FILES = int(environ.get("MAX_FILES", "10"))

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in environ.get('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in environ.get('BAN_CHNL', '').split()]
BAN_ALERT = environ.get('BAN_ALERT' , '')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', '')
DATABASE_NAME = environ.get('DATABASE_NAME', 'FileStream')

# fsub information
AUTH_PICS = environ.get('AUTH_PICS', '')
AUTH_CHANNEL = environ.get("AUTH_CHANNEL", "")
FSUB = environ.get("FSUB", True)

# port information
PORT = int(getenv('PORT', '2626'))
NO_PORT = bool(getenv('NO_PORT', False))

# time information
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADDRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', ''))
APP_NAME = None

if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False

FQDN = str(getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
HAS_SSL = bool(getenv('HAS_SSL', False))
URL = str(getenv('URL', ''))
