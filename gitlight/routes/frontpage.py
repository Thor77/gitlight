#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
==========
Front Page
==========

Basic route for handling the front page.
'''
# Python / Flask Imports
import flask

# GitLight Imports
from gitlight.mods import frontpage

# Blueprint: frontpage
bp = flask.Blueprint('frontpage', __name__)


@bp.route('/', methods=['GET', 'HEAD'])
def index():
    '''
    Return a pretty rendering of the front page.
    '''
    return flask.render_template('gitlight/index.html', body=frontpage.build())
