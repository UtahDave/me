#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''me

Usage:
  me list
  me add <item>
  me delete <item>
  me finish <item>
  me -h | --help
  me --version

Options:
  -h --help     Show this screen.
  --version     Show version.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

#import me libs

import me.utils

__version__ = "0.1.0"
__author__ = "David Boucha"
__license__ = "Apache 2.0"


def main():
    '''Main entry point for the me CLI.'''
    args = docopt(__doc__, version=__version__)
    me.utils.verify_env()
    opts = me.utils.load_opts()
    print(args)

if __name__ == '__main__':
    main()
