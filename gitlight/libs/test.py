#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
====
Test
====

Library for running arbitrary tests.
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


def sleep(seconds):
    '''
    Pause execution for <seconds> seconds.

    Usage: 

    .. code-block:: python

        test.sleep(60)
    '''
    if int(seconds) <= 0:
        return False
    time.sleep(int(seconds))
    return True


def sleep_r(seconds=60):
    '''
    Pause execution for a random amount of time, between 1 and <seconds> seconds.

    Usage: 

    .. code-block:: python

        test.sleep_r(180)
    '''
    if int(seconds) <= 0:
        return False
    time.sleep(random.randint(1, seconds))
    return True
