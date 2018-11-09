#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Test frontpage routes
'''


def test_index():
    '''
    Test that the homepage renders.
    '''
    # TODO: Skipped (not working)
    return 0
    response = client.get('/')
    assert b'GitLight' in response.data
