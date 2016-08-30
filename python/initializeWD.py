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

from add_to_matlab_startup import add_to_matlab_startup
from synchronizeGit import origin2masterUpdate, master2originUpdate

# synchronize with github

user = 'LucaDiStasio'
pwd = 'dylan666'

wd = 'D:/01_Luca/03_DocMASE/04_WD'

origin2masterUpdate(wd,user)
master2originUpdate(wd,user,pwd)

# update Matlab startup file

userName = 'Luca'
matlabRoot = 'C:\\Program Files\\MATLAB\\R2012a'
workdir = 'D:\\01_Luca\\03_DocMASE\\04_WD'

add_to_matlab_startup(userName,matlabRoot,workdir)