# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2017
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

Automatic translation of CV in Latex format.

Tested with Python 3.5 Anaconda 3 (64-bit) distribution
       in Windows 7.

'''

from os import listdir
from os.path import isfile, join

overWrite = True

mainFolder = 'D:\\OneDrive\\01_Luca\\02_Professional_documents\\01_Curriculum_Vitae'

type = 'CV'

source = 'en'

target = 'es'

sourceFolder = ''

targetFolder = ''

sourceFile = ''

dictionary = {
              'en':'english',
              'fr':'francais',
              'es':'espanol',
              'it':'italiano',
              'de':'deutsch',
             }

for folder in listdir(mainFolder):
    if source in folder:
        sourceFolder = join(mainFolder,folder,listdir(join(mainFolder,folder))[0])
        for file in listdir(sourceFolder):
            if type + '_' + dictionary[source] + '.tex'==file:
                sourceFile = join(sourceFolder,file)
    if target in folder:
        if overWrite:
            targetFolder = join(mainFolder,folder,listdir(join(mainFolder,folder))[0])
            for file in listdir(targetFolder):
                if type + '_' + dictionary[target] + '.tex'==file:
                    targetFile = join(targetFolder,file)
        else:
            targetFolder = join(mainFolder,folder)
            targetFile = join(targetFolder,type + '_' + dictionary[target] + '.tex')
        
with open(sourceFile,'r') as file:
    lines = file.readlines()
    
toTranslate = []

docStart = 0
endDoc = len(lines)

for i,line in enumerate(lines):
    if '\\begin{document}' in line:
        docStart = i
    elif '\\end{document}' in line:
        endDoc = i

for i in range(docStart+1,endDoc):
    toTranslate.append(lines[i])
    
for line in toTranslate:
    print(line)
