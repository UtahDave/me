#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Common utilities
'''

#import python libs
import os
from os.path import expanduser
import yaml
from __future__ import unicode_literals, print_function

HOME = expanduser('~')
TASKFILEPATH = os.path.join(HOME, '.me')


def verify_env():
    '''
    Make sure that all required files exist
    '''

    # make sure ~/.me path exists
    if not os.path.exists(TASKFILEPATH):
        os.makedirs(TASKFILEPATH)

    # make sure default tasks.sls file exists
    if not os.path.isfile(os.path.join(TASKFILEPATH, 'tasks.sls')):
        with open(os.path.join(TASKFILEPATH, 'tasks.sls'), 'w') as taskfile:
            taskfile.write('taskfile')

    # make sure default config exists
    if not os.path.isfile(os.path.join(TASKFILEPATH, 'config.sls')):
        config = {}
        config['configfile'] = os.path.join(TASKFILEPATH, 'config.sls')
        config['taskfile'] = os.path.join(TASKFILEPATH, 'tasks.sls')
        with open(os.path.join(TASKFILEPATH, 'config.sls'), 'w') as configfile:
            configfile.write(yaml.dump(config, default_flow_style=False))


def load_opts(configfile=None):
    '''
    Load the config file
    '''
    opts = {}
    if not configfile:
        configfile = os.path.join(TASKFILEPATH, 'config.sls')
    with open(configfile, 'r') as yaml_file:
        opts = yaml.safe_load(yaml_file)
    opts = dict(opts)
    print(opts)
    return opts

