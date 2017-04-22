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

Automatic translation of Latex documents.

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution
       in Windows 10.

'''

from os import listdir
from os.path import isfile, join
import numpy
import cv2
try:
    import Image
except ImportError:
    from PIL import Image
from pytesseract import image_to_string


wd = 'C:\\01_Backup-folder\\GoogleDrive\\receipts'

fileFormat = 'jpg'

files = []
for file in listdir(wd):
    if file.split('.')[1]==fileFormat:
        files.append(file)

for file in files:
    print join(wd,file)
    print image_to_string(Image.open(join(wd,file)))