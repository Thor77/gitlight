'''
GitLight Application
'''
from flask import Blueprint
from . import routes

gitlight = Blueprint('gitlight', __name__) # pylint: disable=invalid-name
