#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2016-2017 Université de Lorraine & Luleå tekniska universitet
Author: Luca Di Stasio <luca.distasio@gmail.com>
                       <luca.distasio@ingpec.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

=====================================================================================

DESCRIPTION



Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution in Windows 7.

'''

from os import listdir, remove
from os.path import isfile, join, getmtime
import sys
import getopt
from datetime import datetime
from time import strftime

def main(argv):

    # Read the command line, throw error if not option is provided
    try:
        opts, args = getopt.getopt(argv,'hw:e:d:',["help","Help","user", "workdir", "workdirectory", "wdir", "ext","extension","delay"])
    except getopt.GetoptError:
        print('fileCleaner.py -w <working directory> -e <extension> -d <delay>')
        sys.exit(2)
    # Parse the options and create corresponding variables
    for opt, arg in opts:
        if opt in ('-h', '--help','--Help'):
            print(' ')
            print(' ')
            print('*****************************************************************************************************')
            print(' ')
            print(' ')
            print('                                        FILES CLEANER')
            print(' ')
            print('                                              by')
            print(' ')
            print('                                    Luca Di Stasio, 2016-2017')
            print(' ')
            print(' ')
            print('*****************************************************************************************************')
            print(' ')
            print('Program syntax:')
            print('fileCleaner.py  -w <working directory> -e <extension> -d <delay>')
            print(' ')
            print('Mandatory arguments:')
            print('-w <working directory>')
            print(' ')
            print('Optional arguments:')
            print('-e <extension>')
            print('-d <delay>')
            print(' ')
            print('Default values:')
            print('<extension>              ========>           .log')
            print('<delay>                  ========>           24 hours (always provide hours)')
            print(' ')
            print(' ')
            sys.exit()
        elif opt in ("-w", "--workdir", "--workdirectory", "--wdir"):
            if arg[-1] != '/':
                workdir = arg
            else:
                workdir = arg[:-1]
        elif opt in ("-e", "--ext","--extension"):
            if '.'==arg[0]:
                ext = arg
            else:
                ext = '.' + arg
        elif opt in ("-e", "--ext","--extension"):
            delay = int(arg)

    # Check the existence of variables: if a required variable is missing, an error is thrown and program is terminated; if an optional variable is missing, it is set to the default value
    if 'workdir' not in locals():
        print('Error: working directory not provided.')
        sys.exit(2)
    if 'ext' not in locals():
        ext = '.log'
    if 'delay' not in locals():
        delay = 24
    
    files = [f for f in listdir(workdir) if isfile(join(workdir, f)) and ext in f]
    
    now = datetime.now()
    for file in files:
        lastmod = datetime.fromtimestamp(int(getmtime(join(workdir,file))))
        diff = divmod((now - lastmod).total_seconds(), 3600)
        if diff[0]>24:
            remove(join(workdir,file))


if __name__ == "__main__":
    main(sys.argv[1:])