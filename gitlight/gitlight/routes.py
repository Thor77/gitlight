'''
GitLight - Application Routes
'''
from flask import render_template  # request
from . import gitlight

@gitlight.route('/', methods=['GET'])
def index():
    '''Site Index'''
    return render_template('gitlight/index.html')
