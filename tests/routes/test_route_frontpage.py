#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Test frontpage routes
'''


def test_index(client):
    '''
    Test that the homepage renders.
    '''
    response = client.get('/')
    assert b'GitLight' in response.data
