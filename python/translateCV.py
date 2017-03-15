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
import websocket
import thread
import json
import requests
import urllib
import wave
import audioop
from time import sleep
import StringIO
import struct
import sys
import codecs
from xml.etree import ElementTree

#mainFolder = 'D:\\OneDrive\\01_Luca\\02_Professional_documents\\01_Curriculum_Vitae'
#mainFolder = 'C:\\01_Backup-folder\\OneDrive\\01_Luca\\02_Professional_documents\\01_Curriculum_Vitae'

def GetToken(): #Get the access token from ADM, token is good for 10 minutes
    urlArgs = {
        'client_id': 'ENTER YOU CLIENT ID',
        'client_secret': 'ENTER YOUR CLIENT SECRET',
        'scope': 'http://api.microsofttranslator.com',
        'grant_type': 'client_credentials'
    }

    oauthUrl = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'

    try:
        oauthToken = json.loads(requests.post(oauthUrl, data = urllib.urlencode(urlArgs)).content) #make call to get ADM token and parse json
        finalToken = "Bearer " + oauthToken['access_token'] #prepare the token
    except OSError:
        pass

    return finalToken

def translate(token,text,source,target):
    #Call to Microsoft Translator Service
    headers = {"Authorization ": token}
    translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(textToTranslate, toLangCode)
   
    try:
        translationData = requests.get(translateUrl, headers = headers) #make request
        translation = ElementTree.fromstring(translationData.text.encode('utf-8')) # parse xml return values
        print "The translation is---> ", translation.text #display translation

    except OSError:
        pass
    
def main(argv):

    # Read the command line, throw error if not option is provided
    try:
        opts, args = getopt.getopt(argv,'hw:t:s:o:',['help','Help',"inputfile", "workdir", "workdirectory", "wdir","source","target","overwrite"])
    except getopt.GetoptError:
        print('translateCV.py -w <working directory> -t <target language> -s <source language> -o <overwrite>')
        sys.exit(2)
    # Parse the options and create corresponding variables
    for opt, arg in opts:
        if opt in ('-h', '--help','--Help'):
            print(' ')
            print(' ')
            print('*****************************************************************************************************')
            print(' ')
            print(' ')
            print('                         AUTOMATIC CV TRANSLATION IN LATEX FORMAT')
            print(' ')
            print(' ')
            print('                                              by')
            print(' ')
            print('                                    Luca Di Stasio, 2016-2017')
            print(' ')
            print(' ')
            print('*****************************************************************************************************')
            print(' ')
            print('Program syntax:')
            print('translateCV.py -w <working directory> -t <target language> -s <source language> -o <overwrite>')
            print(' ')
            print('Mandatory arguments:')
            print('-w <working directory>')
            print('-t <target language>')
            print(' ')
            print('Optional arguments:')
            print('-s <source language>')
            print(' ')
            print('Default values:')
            print('-s <source language>                ===> english (en)')
            print('-o <overwrite>                      ===> false')
            print(' ')
            print(' ')
            sys.exit()
        elif opt in ("-w", "--workdir", "--workdirectory", "--wdir"):
            if arg[-1] != '/':
                workdir = arg
            else:
                workdir = arg[:-1]
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("-o", "--overwrite"):
            overWrite = True

    # Check the existence of variables: if a required variable is missing, an error is thrown and program is terminated; if an optional variable is missing, it is set to the default value
    if 'workdir' not in locals():
        print('Error: working directory not provided.')
        sys.exit()
    if 'target' not in locals():
        print('Error: target language not provided.')
        sys.exit()
    if 'source' not in locals():
        source = 'en'
    if 'overWrite' not in locals():
        overWrite = False
    
    type = 'CV'
    
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
    
    stopwords = [
                'cventry',
                'cvitem',
                'emph',
                'href',
                'includegraphics',
                'makecvtitle',
                'newpage',
                'section',
                'small',
                'subsection',
                'textbf',
                'textit',
                'vspace'
                ]
    
    for folder in listdir(mainFolder):
        if folder is not 'Archive':
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
        newline = line
        for word in stopwords:
            line = line.replace('\\'+word,' ')
        line = line.replace('{',' ').replace('}',' ')
        if line.replace(' ','')[0] is not '%':
            print(newline.replace(line,translator('en', 'es', line)[0][0][0]))
    






if __name__ == "__main__":
    main(sys.argv[1:])