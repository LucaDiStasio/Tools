#!/usr/bin/env Python
# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2016 Université de Lorraine & Luleå tekniska universitet
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

Automatic initialization of Working Directory.

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution
       Matlab R2007b, R2012a
       Windows 7 Integral Edition, Windows 10.

'''

from os.path import isfile, join
import sys
import getopt
from add_to_matlab_startup import add_to_matlab_startup
from add_to_octave_startup import add_to_octave_startup
from synchronizeGit import origin2masterUpdate, master2originUpdate
from platform import *

def main(argv):

    # Read the command line, throw error if not option is provided
    try:
        opts, args = getopt.getopt(argv,'hu:p:w:m:mu:o:ou:',["help","Help","user", "username","password", "pwd", "pw","workdir", "workdirectory", "wdir","mroot", "matlab", "matlabroot","muser", "matlabuser","oroot", "octave", "octaveroot","ouser", "octaveuser"])
    except getopt.GetoptError:
        print('initializeWD.py -i <input deck> -d <input directory> -w <working directory>  -m <matlab root> -mu <matlab username> -o <octave root> -ou <octave username>')
        sys.exit(2)
    # Parse the options and create corresponding variables
    for opt, arg in opts:
        if opt in ('-h', '--help','--Help'):
            print(' ')
            print(' ')
            print('*****************************************************************************************************')
            print(' ')
            print(' ')
            print('                         AUTOMATIC SYNCHRONIZATION OF WORKING DIRECTORY')
            print(' ')
            print('                                              by')
            print(' ')
            print('                                    Luca Di Stasio, 2016-2017')
            print(' ')
            print(' ')
            print('*****************************************************************************************************')
            print(' ')
            print('Program syntax:')
            print('initializeWD.py -u <user> -p <password> -w <working directory> -m <matlab root> -mu <matlab username> -o <octave root> -ou <octave username>')
            print(' ')
            print('Mandatory arguments:')
            print('-u <user>')
            print('-p <password>')
            print('-w <working directory>')
            print(' ')
            print('Optional arguments:')
            print('-m <matlab root>')
            print('-mu <matlab username>')
            print('-o <octave root>')
            print('-ou <octave username>')
            print(' ')
            print('Default values:')
            print('Matlab startup file will not be updated unless matlab root is provided ')
            print('Octave startup file will not be updated unless matlab root is provided ')
            print('-mu <matlab username>        =====>      GitHub username will be used')
            print('-ou <octave username>        =====>      GitHub username will be used')
            print(' ')
            print(' ')
            sys.exit()
        elif opt in ("-u", "--user", "--username"):
            print arg
            user = arg
        elif opt in ("-p", "--password", "--pwd", "--pw"):
            print arg
            pwd = arg
        elif opt in ("-w", "--workdir", "--workdirectory", "--wdir"):
            print arg
            if arg[-1] != '/':
                workdir = arg
            else:
                workdir = arg[:-1]
        elif opt in ("-m", "--mroot", "--matlab", "--matlabroot"):
            print arg
            if arg[-1] != '/' and arg[-1] != '\\':
                matlabRoot = arg
            else:
                matlabRoot = arg[:-1]
        elif opt in ("-mu", "--muser", "--matlabuser"):
            print arg
            muser = arg
        elif opt in ("-o", "--oroot", "--octave", "--octaveroot"):
            print arg
            if arg[-1] != '/' and arg[-1] != '\\':
                octaveRoot = arg
            else:
                octaveRoot = arg[:-1]
        elif opt in ("-ou", "--ouser", "--octaveuser"):
            ouser = arg

    # Check the existence of variables: if a required variable is missing, an error is thrown and program is terminated; if an optional variable is missing, it is set to the default value
    if 'user' not in locals():
        print('Error: user not provided.')
        sys.exit(2)
    if 'pwd' not in locals():
        print('Error: password not provided.')
        sys.exit(2)
    if 'workdir' not in locals():
        print('Error: working directory not provided.')
        sys.exit(2)
    if 'matlabRoot' not in locals():
        updateMatlab = False
    else:
        updateMatlab = True
    if 'muser' not in locals():
        muser = user
    if 'octaveRoot' not in locals():
        updateOctave = False
    else:
        updateOctave = True
    if 'ouser' not in locals():
        ouser = user
    
    origin2masterUpdate(workdir,user,pwd)
    master2originUpdate(workdir,user,pwd)
    print(matlabRoot)
    if updateMatlab:
        # update Matlab startup file
        add_to_matlab_startup(muser,matlabRoot,workdir)
    
    if updateOctave:
        # update Matlab startup file
        add_to_octave_startup(ouser,octaveRoot,workdir)




if __name__ == "__main__":
    main(sys.argv[1:])