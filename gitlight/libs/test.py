#!/usr/bin/env python3
'''
Module for running arbitrary tests
'''
import random
import time


def echo(text):
    '''
    Return a simple welcome-type message.

    Usage:

    .. code-block:: python

        test.echo('red rum')
    '''
    return text


def sleep(length):
    '''
    Pause execution for <length> seconds.

    Usage: 

    .. code-block:: python

        test.sleep(60)
    '''
    time.sleep(int(length))
    return True


def sleep_r(max=60):
    '''
    Pause execution for a random amount of time, between 0 and <max> seconds.

    Usage: 

    .. code-block:: python

        test.sleep_r(180)
    '''
    time.sleep(random.randint(0, max))
    return True
