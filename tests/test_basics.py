#!/usr/bin/env python3
'''
Test basic site functionality.
'''
import unittest
from flask import current_app
from app import create_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        '''
        Verify gitlight app was found.
        '''
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        '''
        Verify test is running with TESTING config
        '''
        self.assertTrue(current_app.config['TESTING'])

    def test_root(self):
        '''
        Verify the front page renders correctly.
        '''
        response = self.client.get('/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'GitLight?' in response.data)
