#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Common utilities
'''

#import python libs
import os

def verify_env():
    '''
    Make sure that all required files exist
    '''
    print('yes')
    if not os.path.exists('~/.me/'):
        os.mkdir('~/.me/')
