#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Test the frontpage module.
'''
# GitLight Imports
from gitlight.mods import frontpage


def test_build():
    '''
    Test building front page.
    '''
    # Page has expected text
    assert 'GitLight' in frontpage.build()
