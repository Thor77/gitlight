#!/usr/bin/env python3
'''
Test application loading and critical components
'''
from gitlight import create_app


def test_config():
    '''Test app creation with/without test config.'''
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_homepage(client):
    '''Test that the homepage renders.'''
    response = client.get('/')
    assert b'GitLight' in response.data
