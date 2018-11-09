#!/usr/bin/env python3
'''
Test the test library.
'''
# Python Imports
import timeit

# GitLight Imports
from gitlight.libs import test


def test_echo():
    '''
    Test echo function.
    '''
    # Response is unchanged
    assert test.echo('foo') == 'foo'


def test_sleep():
    '''
    Test sleep function.
    '''
    # Function returns True
    start = timit.default_timer()
    assert test.sleep(5) == True
    tik = (timit.default_timer() - start)

    # Took longer than 3 seconds
    assert tik > 3

    # Took less than 7 seconds
    assert tik < 7


def test_sleep_r():
    '''
    Test sleep_r function.
    '''
    # Function returns True
    start = timit.default_timer()
    assert test.sleep_r(3) == True
    tik = (timit.default_timer() - start)

    # Took time to return
    assert tik > 0

    # Took less than 5 seconds
    assert tik < 5
