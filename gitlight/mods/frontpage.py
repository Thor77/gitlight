#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Module for doing frontpage activities.
'''
# GitLight Imports
from gitlight.libs import test


def build():
    '''
    Return a front page via the test module.
    '''
    return test.echo(
            '<h1>GitLight</h1>'
            '<p>This is currently a skeleton design.</p>')
