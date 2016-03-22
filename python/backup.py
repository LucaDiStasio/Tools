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

Uncompressed backup from local hard disk to freely accessible hard disk located on LAN

The script walk through a given directory and store all the directories, subdirectories 
and files. It then checks in the destination the existence of each of them; if they do
not exist, it creates the folder/subfolder and copy the file

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution in Windows 10.

'''

import sys, os
from time import strftime
from shutil import copyfile, rmtree

def ucmpbackup(source,destination):
    now = strftime("%Y-%m-%d_%H-%M-%S")
    wd = os.getcwd()
    log = wd + '\\' + now + '_backup.log'
    
    with open(log, 'w') as file:
        file.write('UNCOMPRESSED BACKUP\n')
        file.write('Started on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S") + '\n')
        file.write('SOURCE:     ' + source + '\n')
        file.write('DESTINATION:    ' + destination + '\n')
        file.write('\n')
    
    print "Copying from ..."
    print ''
    for dirName, subdirList, files in os.walk(source):
        print '     ' + dirName
        if not os.path.exists(destination + '\\' + dirName.split('\\')[-1]) and not os.path.exists("\\".join(destination.split('\\')[:-1]) + '\\' + dirName.split('\\')[-1]):
            os.makedirs(destination + '\\' + dirName.split('\\')[-1])
            with open(log, 'a') as file:
                file.write(strftime("%H:%M:%S") + ' - Created FOLDER:    ' + destination + '\\' + dirName.split('\\')[-1] + '\n')
        for file in files:
            subdir = ''
            folderList = dirName.split('\\')
            for i,folder in enumerate(folderList):
                if folder == destination.split('\\')[-1]:
                    index = i
                    break
            if not index == len(folderList)-1:
                subdir += "\\".join(dirName.split('\\')[index+1:])
            if not subdir ==  '':
                endPath =  "\\" + subdir + "\\" + file
            else:
                endPath =  "\\" + file
            src = dirName + '\\' +  file
            dst = destination + endPath 
            if not os.path.exists(dst):
                copyfile(src, dst)
                with open(log, 'a') as file:
                    file.write(strftime("%H:%M:%S") + ' - Copied FILE:    ' + str(file) + ' to ' + "/".join(dst.split('\\')[:-1]) + '\n')
    
    print ''
    print 'Checking old files and folders to be removed from ...'
    for dirName, subdirList, files in os.walk(destination):
        print '     ' + dirName
        if not os.path.exists(source + '\\' + dirName.split('\\')[-1]) and not os.path.exists("\\".join(source.split('\\')[:-1]) + '\\' + dirName.split('\\')[-1]):
            rmtree(dirName)
            with open(log, 'a') as file:
                file.write(strftime("%H:%M:%S") + ' - Removed FOLDER:    ' + dirName + '\n')
        else:
            for file in files:
                subdir = ''
                folderList = dirName.split('\\')
                for i,folder in enumerate(folderList):
                    if folder == source.split('\\')[-1]:
                        index = i
                        break
                if not index == len(folderList)-1:
                    subdir += "\\".join(dirName.split('\\')[index+1:])
                if not subdir ==  '':
                    endPath =  "\\" + subdir + "\\" + file
                else:
                    endPath =  "\\" + file
                dst = dirName + '\\' +  file
                src = source + endPath 
                if not os.path.exists(src):
                    os.remove(dst)
                    with open(log, 'a') as file:
                        file.write(strftime("%H:%M:%S") + ' - Removed FILE:    ' + str(file) + ' from ' + "/".join(dst.split('\\')[:-1]) + '\n')    
 
 
sourceFolder = 'C:\\01_Luca\\11_Ordine_degli_Ingegneri_Milano'
destinationFolder = '\\\\BBOX\\Volume\\01_Luca\\11_Ordine_degli_Ingegneri_Milano' 

ucmpbackup(sourceFolder,destinationFolder)      