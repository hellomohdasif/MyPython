try:
    import settings_dev
except:
    print("No development mode settings found.")
    settings_dev = None

# API Authentication Settings
ACCESS_ID = settings_dev.ACCESS_ID if settings_dev else 'mozscape-eefcc18ce4'
SECRET_KEY = settings_dev.SECRET_KEY if settings_dev else 'c4ec09f9740b4838be2892e1878f7b52'
REQUEST_INTERVAL = 11  # Number of seconds between each Moz request.

# Threshold Settings
MINIMUM_MOZRANK =3
MINIMUM_DA = 20
MINIMUM_PA = 20

# Database
DB_NAME = 'data.db'

# Reporting
OUT_DIR = './output/'