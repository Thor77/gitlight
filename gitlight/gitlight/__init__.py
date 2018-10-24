'''
GitLight Application
'''
from flask import Blueprint

gitlight = Blueprint('gitlight', __name__)

from . import routes
