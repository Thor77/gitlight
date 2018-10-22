'''
GitLight - Application Routes
'''
#from flask import request, render_template
from flask import render_template
from . import gitlight

@gitlight.route('/', methods=['GET'])
def index():
    '''Site Index'''
    return render_template('gitlight/index.html')
