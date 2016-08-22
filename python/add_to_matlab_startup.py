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

import sys, os;

def add_to_matlab_startup(userName,matlabRoot,WD):
    matlabpathDir = '\\toolbox\\local'
    matlabpathdef = '\\pathdef.m'
    matlabstartup = '\\startup.m'
    
    dirs = []
    for dirName, subdirList, files in os.walk(WD):
        if ".git" not in dirName:
            dirs.append(dirName)
    
    matlabpath = matlabRoot + matlabpathDir + matlabpathdef
    matlabstart = matlabRoot + matlabpathDir + matlabstartup
    toAdd = []
    toWrite = []
    
    with open(matlabpath, 'r') as file:
        lines = file.readlines()
    
    check = False
    for i, line in enumerate(lines):
        if not check:
            toWrite.append(line)
        if "CUSTOM ENTRIES" in line and "END ENTRIES" not in lines[i+1]:
            check = True
        if "CUSTOM ENTRIES" not in line and "END ENTRIES" not in line and check:
            if os.path.exists(line[6:-8]):
                toWrite.append(line)
            else:
                print "Directory " + line[6:-8] + " does not exist and will be removed"
        if "END ENTRIES" in line and check:
            check = False
            toWrite.append(line)
    
    
    for dir in dirs:
        add = True
        for line in toWrite:
            if dir in line:
                add = False
                break
        if add:
            toAdd.append(dir)
    
    with open(matlabstart, 'w') as file:
        file.write("disp('Hi, " + userName + "!');\n")
        file.write("disp('Welcome back!');\n")
        file.write("disp('I''m adding the following directories to the path:');\n")
        print "Adding:"
        for dir in toAdd:
            print dir
            file.write("disp('      " + dir + "');\n") 
            file.write("addpath('" + dir + "','-end');\n")

'''
userName1 = 'Luca'
matlabRoot1 = 'C:\\Program Files\\MATLAB\\R2007b'
WD1 = 'C:\\01_backup-folder\\OneDrive\\01_Luca\\07_DocMASE\\04_WD'
add_to_matlab_startup(userName1,matlabRoot1,WD1)
'''