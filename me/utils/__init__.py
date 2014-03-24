#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Common utilities
'''

#import python libs
import os
from os.path import expanduser

def verify_env():
    '''
    Make sure that all required files exist
    '''
    print('yes')
    home = expanduser('~')
    print(home)
    taskfilepath = os.path.join(home, '.me')
    print(taskfilepath)
    if not os.path.exists(taskfilepath):
        os.makedirs(taskfilepath)
    if not os.path.isfile(os.path.join(taskfilepath, 'tasks.sls')):
        with open(os.path.join(taskfilepath, 'tasks.sls'), 'w') as taskfile:
            taskfile.write('taskfile')
