#!/usr/ben/env python3
'''
Production Settings
'''
import os

DEBUG = False

# Gitolite3 Configuration File
G3_CONF = os.environ.get('GL_CONF')
# Gitolite3 Home Directory
G3_HOME = os.environ.get('GL_HOME')

# GitLight Command
GL_BIN = os.environ.get('GL_BIN')

# Database Engine
DB_ENGINE = os.environ.get('DB_ENGINE')
# Sqlite3 File
DB_FILE = os.environ.get('DB_FILE')
# Database Host
DB_HOST = os.environ.get('DB_HOST')
# Database Port
DB_PORT = os.environ.get('DB_PORT')
# Database User
DB_USER = os.environ.get('DB_USER')
# Database Pass
DB_PASS = os.environ.get('DB_PASS')
