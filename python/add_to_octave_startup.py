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

GitHub versioning with Matlab

The script walk through the user-provided working directory (where it is saved) and save all
the directories and subdirectories. It then reads the Matlab pathdef.m file and check
if user-defined entries (if any) exist. Finally, it adds the addpath command for
each directory and subdirectory of the WD to the startup.m file, which is then executed
automatically by Matlab.

It simplifies versioning (with gitHUb, for example) as it allows to adjust the local
Matlab settings to new repositories or changes in repository structure.

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution
       and  Matlab R2007b
       in Windows 10.

Change the <matlabRoot> variable to adjust for distribution of preference.

'''

import sys, os
from os.path import isfile, join
from datetime import datetime
from time import strftime

def add_to_octave_startup(userName,root,WD):
    octavepathDir = '\\share\\octave\\' + root.split('\\')[-1].split('-')[-1] + '\\m\\startup'
    octavestartup = '\\octavestartup.m'
    
    dirs = []
    for dirName, subdirList, files in os.walk(WD):
        if ".git" not in dirName:
            dirs.append(dirName)
    
    octavestart = join(root,octavepathDir,octavestartup)

    try:
        with open(octavestart, 'w') as file:
            file.write("disp('Hi, " + userName + "!');\n")
            file.write("disp('Welcome back!');\n")
            file.write("disp('I''m adding the following directories to the path:');\n")
            if isfile(join(WD,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
                with open(join(WD,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
                    #print("")
                    #print("Adding:")
                    logfile.write("\n")
                    logfile.write("Adding:\n")
                    for dir in dirs:
                        #print(dir)
                        logfile.write(dir+'\n')
                        file.write("disp('      " + dir + "');\n") 
                        file.write("addpath('" + dir + "','-end');\n")
            else:
                with open(join(WD,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
                    #print("")
                    #print("Adding:")
                    logfile.write("\n")
                    logfile.write("Adding:\n")
                    for dir in dirs:
                        #print(dir)
                        logfile.write(dir+'\n')
                        file.write("disp('      " + dir + "');\n") 
                        file.write("addpath('" + dir + "','-end');\n")
    except Exception,e:
        if isfile(join(WD,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
            with open(join(WD,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                      v\n')
                logfile.write('^                        ERROR OCCURRED                                v\n')
                logfile.write('^    IN FUNCTION add_to_octave_startup in add_to_octave_startup.py     v\n')
                logfile.write('^                                                                      v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write(str(e)+'\n')
                logfile.write('\n')
        else:
            with open(join(WD,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                      v\n')
                logfile.write('^                        ERROR OCCURRED                                v\n')
                logfile.write('^    IN FUNCTION add_to_octave_startup in add_to_octave_startup.py     v\n')
                logfile.write('^                                                                      v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write(str(e)+'\n')
                logfile.write('\n')
        sys.exc_clear()
    
  