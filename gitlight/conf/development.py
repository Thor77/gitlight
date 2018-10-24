import os

# Disable Debug
DEBUG=False
# Enable Testing
TESTING=True
# Need a DB
DB_ENGINE=os.environ.get('DB_ENGINE', 'sqlite3')
# Chose Sqlite
DB_FILE=os.environ.get('DB_FILE', '/tmp/gitlight.sql')
