# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2017 Université de Lorraine & Luleå tekniska universitet
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

Automatic fix to Git conflicts.

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution
       in Windows 7.

'''

from os import listdir
from os.path import isfile, join

def lookForConflicts(lines,rightVersion):
    conflicts = []
    conflict = []
    for i,line in enumerate(lines):
        if '<<<<<<<' in line:
            version = line.split()[1]
            if version == rightVersion:
                conflict.append([i,version,True])
            else:
                conflict.append([i,version,False])
            version = ''
        elif '=======' in line and '%' not in line:
            conflict.append(i)
        elif '>>>>>>>' in line:
            version = line.split()[1]
            if version == rightVersion:
                conflict.append([i,version,True])
            else:
                conflict.append([i,version,False])
            version = ''
            conflicts.append(conflict)
            conflict = []
    return conflicts

def defineRightVersion(lines,conflict,conflictnumber):
    print ' '
    print '======================================================================================'
    print 'Conflict ' + str(conflictnumber+1)
    print ' '
    print '---------------------------------------------------------------'
    print 'First version: ' + conflict[0][1]
    print ' '
    for line in lines[conflict[0][0]+1:conflict[1]]:
        print ' || ' + line
    print ' '
    print '---------------------------------------------------------------'
    print 'Second version: ' + conflict[2][1]
    print ' '
    for line in lines[conflict[1]+1:conflict[2][0]]:
        print ' || ' + line
    if conflict[0][2]:
        print ' '
        print '====> Selected version: ' +  conflict[0][1] + ' <===='
        solution=[[conflict[0][0],conflict[2][0]],[conflict[0][0],conflict[1]]]
    elif conflict[2][2]:
        print ' '
        print '====> Selected version: ' +  conflict[2][1] + ' <===='
        solution=[[conflict[0][0],conflict[2][0]],[conflict[1],conflict[2][0]]]
    else:
        print ' '
        print '====> No version is deemed correct. Check the input or fix the conflict manually. <===='
        solution=[[conflict[0][0],conflict[2][0]],[conflict[0][0],conflict[2][0]]]
    return solution

def solveConflict(lines,startConflictSection,endConflictSection,startSolutionSection,endSolution):
    text = []
    if startConflictSection==0:
        for line in lines[startSolutionSection+1:endSolution]:
            text.append(line)
        for line in lines[endConflictSection+1:]:
            text.append(line)
    elif endConflictSection==len(lines)-1:
        for line in lines[:startConflictSection]:
            text.append(line)
        for line in lines[startSolutionSection+1:endSolution]:
            text.append(line)
    else:
        for line in lines[:startConflictSection]:
            text.append(line)
        for line in lines[startSolutionSection+1:endSolution]:
            text.append(line)
        for line in lines[endConflictSection+1:]:
            text.append(line)
    return text

def solveVersionConflicts(folder,file,version):
    with open(join(folder,file),'r') as f:
        lines = f.readlines()
    conflicts = lookForConflicts(lines,version)
    nConflicts = len(conflicts)
    count = 0
    while nConflicts>0:
        print ' '
        print '======================================================================================'
        print '======================================================================================'
        print ' '
        print '           ITERATION ' + str(count+1) + ' ON FILE ' + file
        print '                  ' + str(nConflicts) + ' CONFLICTS FOUND IN TOTAL'
        print ' '
        print '======================================================================================'
        print '======================================================================================'
        rightVersion = defineRightVersion(lines,conflicts[0],count)
        lines = solveConflict(lines,rightVersion[0][0],rightVersion[0][1],rightVersion[1][0],rightVersion[1][1])
        conflicts = lookForConflicts(lines,version)
        nConflicts = len(conflicts)
        count+=1
    print ''
    print '======================================================================================'
    print '======================================================================================'
    print ' '
    print '           NO MORE CONFLICTS FOUND IN FILE ' + file
    print ' '
    print '======================================================================================'
    print '======================================================================================'
    print ''
    print '======================================================================================'
    print '======================================================================================'
    print ' '
    print '            AMENDED TEXT IN FILE ' + file
    print ' '
    print '======================================================================================'
    print '======================================================================================'
    print ''
    with open(join(folder,file),'w') as f:
        for line in lines:
            print line
            f.write(line)
    



targetFolder = 'D:/OneDrive/01_Luca/07_DocMASE/06_WD/transpilers/matlab/matlab2abaqus'

targetFiles = [f for f in listdir(targetFolder)]

correctVersion = 'HEAD'

for file in targetFiles:
    print ' '
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print '                 WORKING ON FILE ' + file
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    print ' '
    solveVersionConflicts(targetFolder,file,correctVersion)
    
    
        