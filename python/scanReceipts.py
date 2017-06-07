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
from datetime import datetime
from time import strftime
import getopt
import websocket
import thread
import json
import requests
import urllib
import numpy as np
import cv2
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

'''
def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype = "float32")
 
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
 
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    vdiff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(vdiff)]
    rect[3] = pts[np.argmax(vdiff)]
 
    # return the ordered coordinates
    return rect

def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
 
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
 
    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
 
    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
 
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
 
    # return the warped image
    return warped

cv2.destroyAllWindows()

wd = 'C:\\01_Backup-folder\\GoogleDrive\\receipts'
#wd = 'D:\\GoogleDrive\\receipts'

fileFormat = 'jpg'

files = []
for file in listdir(wd):
    if file.split('.')[1]==fileFormat:
        files.append(file)


image = cv2.imread(join(wd,file),0)    
pts = np.array([(73, 239), (356, 117), (475, 265), (187, 443)], dtype = "float32")

warped = four_point_transform(image, pts)

cv2.imshow("Receipt", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)

for file in files[:1]:
    #image = cv2.imread(join(wd,file),0)
    #cv2.imshow("Receipt", image)
    #cv2.waitKey(0)
    print(join(wd,file))
    print(pytesseract.image_to_string(Image.open(join(wd,file)),lang='fra',config="-psm 6"))

cv2.destroyAllWindows()
'''

def GetToken(key): #Get the access token from ADM, token is good for 10 minutes
    authUrl = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    authHeaders = {'Ocp-Apim-Subscription-Key': key}
    authResponse = requests.post(authUrl, headers=authHeaders)
    authToken = authResponse.text
    return authToken