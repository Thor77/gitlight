import os

DEBUG=False
TESTING=True
DB_ENGINE=os.environ.get('DB_ENGINE', 'sqlite3')
DB_FILE=os.environ.get('DB_FILE', '/var/lib/gitlight/data.sqlite3')
