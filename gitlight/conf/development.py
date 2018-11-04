#!/usr/ben/env python3
'''
Development Settings
'''
import os

# Disable Debug
DEBUG = False
# Enable Testing
TESTING = True
# Need a DB
DB_ENGINE = os.environ.get('DB_ENGINE', 'sqlite3')
# Chose Sqlite
DB_FILE = os.environ.get('DB_FILE', '/var/lib/gitlight/data.sqlite3')
