#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''me

Usage:
  me ship new <name>...
  me ship <name> move <x> <y> [--speed=<kn>]
  me ship shoot <x> <y>
  me mine (set|remove) <x> <y> [--moored|--drifting]
  me -h | --help
  me --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''

from __future__ import unicode_literals, print_function
from docopt import docopt

__version__ = "0.1.0"
__author__ = "David Boucha"
__license__ = "Apache 2.0"


def main():
    '''Main entry point for the me CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()
