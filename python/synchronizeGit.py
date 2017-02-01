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

Automatic synchronization of Working Directory with GitHub repositories

Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution in Windows 10.

'''

import sys
import os
from os.path import isfile, join
from datetime import datetime
from github import Github
from git import Git, Repo, InvalidGitRepositoryError
from time import strftime
from platform import system
import subprocess

def listAllUserPublicRepos(user,pwd):
    repos = []
    g = Github(user,pwd)
    for repo in g.get_user().get_repos():
        try:
            repos.append(repo.name)
        except Exception:
            if isfile(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
                with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^    IN FUNCTION listAllUserPublicRepos in synchronizeGit.py     v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
            else:
                with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^    IN FUNCTION listAllUserPublicRepos in synchronizeGit.py     v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
            sys.exc_clear()
    return repos
    
def listDirsInWD(wd):
    dirs = []
    try:
        elements = os.listdir(wd)
    except Exception:
        elements = []
        if isfile(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
            with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                v\n')
                logfile.write('^                        ERROR OCCURRED                          v\n')
                logfile.write('^        IN FUNCTION listDirsInWD in synchronizeGit.py           v\n')
                logfile.write('^                                                                v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write(str(Exception)+'\n')
                logfile.write('\n')
        else:
            with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                v\n')
                logfile.write('^                        ERROR OCCURRED                          v\n')
                logfile.write('^        IN FUNCTION listDirsInWD in synchronizeGit.py           v\n')
                logfile.write('^                                                                v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write(str(Exception)+'\n')
                logfile.write('\n')
        sys.exc_clear()
    for element in elements:
        if os.path.isdir(wd + '/' + element):
            dirs.append(element)
    return dirs

def checkIfDirIsRepo(wd,dir):
    isRepo = False
    path = wd + '/' + dir
    try:
        Repo(path)
        isRepo = True
    except InvalidGitRepositoryError:
        isRepo = False
        if isfile(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
            with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                v\n')
                logfile.write('^                        ERROR OCCURRED                          v\n')
                logfile.write('^        IN FUNCTION checkIfDirIsRepo in synchronizeGit.py       v\n')
                logfile.write('^                                                                v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write('  \n')
                logfile.write(' FOLDER '+ dir +' IN WORKING DIRECTORY ' + wd +'\n')
                logfile.write('  \n')
                logfile.write(str(InvalidGitRepositoryError)+'\n')
                logfile.write('\n')
        else:
            with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                v\n')
                logfile.write('^                        ERROR OCCURRED                          v\n')
                logfile.write('^        IN FUNCTION checkIfDirIsRepo in synchronizeGit.py       v\n')
                logfile.write('^                                                                v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write('  \n')
                logfile.write(' FOLDER '+ dir +' IN WORKING DIRECTORY ' + wd +'\n')
                logfile.write('  \n')
                logfile.write(str(InvalidGitRepositoryError)+'\n')
                logfile.write('\n')
        sys.exc_clear()
    return isRepo

def listReposInWD(wd):
    repos = []
    dirs = listDirsInWD(wd)
    for dir in dirs:
        if checkIfDirIsRepo(wd,dir):
            repos.append(dir)
    return repos

def master2originUpdate(wd,user,pwd):
    userrepos = listAllUserPublicRepos(user,pwd)
    localrepos = listReposInWD(wd)
    if isfile(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
        with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
            for repo in userrepos:
                if repo in localrepos:
                    '''
                    print('')
                    print('=============================')
                    print(repo)
                    print('Pulling...')
                    '''
                    logfile.write('\n')
                    logfile.write('============================='+'\n')
                    logfile.write(repo+'\n')
                    logfile.write('Pulling...'+'\n')
                    path = wd + '/' + repo
                    try:
                        currRepo = Repo(path)
                    except Exception,e:
                        currRepo = ''
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    try:
                        currRepo.remotes.origin.pull()
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    '''
                    print('...done.')
                    print(currRepo.git.status())
                    print('=============================')
                    '''
                    logfile.write('...done.')
                    try:
                        logfile.write(currRepo.git.status()+'\n')
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    logfile.write('============================='+'\n')
                else:
                    '''
                    print('=============================')
                    print(repo)
                    print('Cloning...')
                    '''
                    logfile.write('============================='+'\n')
                    logfile.write(repo+'\n')
                    logfile.write('Cloning...'+'\n')
                    try:
                        remote = 'https://github.com' + '/' + user + '/' + repo
                        local = wd + '/' + repo
                        currRepo = Repo.clone_from(remote, local)
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    '''
                    print('...done.')
                    print(currRepo.git.status())
                    print('=============================')
                    '''
                    logfile.write('...done.')
                    logfile.write('Changing remote url of repo...')
                    changeUrlFile = 'changeGitUrl'
                    if system() is 'Windows':
                        changeUrlFile += '.cmd'
                    elif system() is 'Linux':
                        changeUrlFile += '.sh'
                    changeUrlFilePath = join(wd,changeUrlFile)
                    with open(changeUrlFilePath,'w') as cli:
                        if system() is 'Linux':
                            cli.write('#!/bin/bash\n')
                            cli.write('\n')
                        cli.write('cd ' + local + '\n')
                        cli.write('\n')
                        cli.write('git remote set-url origin https://' + user + ':' + pwd + '@github.com/' + user + '/' + repo + '.git\n')
                    try:
                        if system() is 'Windows':
                            subprocess.call('cmd.exe /C ' + changeUrlFilePath,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                        elif system() is 'Linux':
                            subprocess.call('chmod a+x ' + changeUrlFilePath,shell=True)
                            subprocess.call(changeUrlFilePath)
                        logfile.write('...done.')
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write('\n')
                        logfile.write('Unable to change remote address\n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                    os.remove(changeUrlFilePath)
                    try:
                        logfile.write(currRepo.git.status()+'\n')
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')       
                        sys.exc_clear()
                    logfile.write('=============================')
    else:
        with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
            for repo in userrepos:
                if repo in localrepos:
                    '''
                    print('')
                    print('=============================')
                    print(repo)
                    print('Pulling...')
                    '''
                    logfile.write('\n')
                    logfile.write('============================='+'\n')
                    logfile.write(repo+'\n')
                    logfile.write('Pulling...'+'\n')
                    path = wd + '/' + repo
                    try:
                        currRepo = Repo(path)
                    except Exception,e:
                        currRepo = ''
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    try:
                        currRepo.remotes.origin.pull()
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    '''
                    print('...done.')
                    print(currRepo.git.status())
                    print('=============================')
                    '''
                    logfile.write('...done.')
                    try:
                        logfile.write(currRepo.git.status()+'\n')
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    logfile.write('=============================')
                else:
                    '''
                    print('=============================')
                    print(repo)
                    print('Cloning...')
                    '''
                    logfile.write('============================='+'\n')
                    logfile.write(repo+'\n')
                    logfile.write('Cloning...'+'\n')
                    try:
                        remote = 'https://github.com' + '/' + user + '/' + repo
                        local = wd + '/' + repo
                        currRepo = Repo.clone_from(remote, local)
                    except Exception,e:
                        currRepo = ''
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    '''
                    print('...done.')
                    print(currRepo.git.status())
                    print('=============================')
                    '''
                    logfile.write('...done.'+'\n')
                    logfile.write('Changing remote url of repo...')
                    changeUrlFile = 'changeGitUrl'
                    if system() is 'Windows':
                        changeUrlFile += '.cmd'
                    elif system() is 'Linux':
                        changeUrlFile += '.sh'
                    changeUrlFilePath = join(wd,changeUrlFile)
                    with open(changeUrlFilePath,'w') as cli:
                        if system() is 'Linux':
                            cli.write('#!/bin/bash\n')
                            cli.write('\n')
                        cli.write('cd ' + local + '\n')
                        cli.write('\n')
                        cli.write('git remote set-url origin https://' + user + ':' + pwd + '@github.com/' + user + '/' + repo + '.git\n')
                    try:
                        if system() is 'Windows':
                            subprocess.call('cmd.exe /C ' + changeUrlFilePath,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                        elif system() is 'Linux':
                            subprocess.call('chmod a+x ' + changeUrlFilePath,shell=True)
                            subprocess.call(changeUrlFilePath)
                        logfile.write('...done.')
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write('\n')
                        logfile.write('Unable to change remote address\n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                    os.remove(changeUrlFilePath)
                    try:
                        logfile.write(currRepo.git.status()+'\n')
                    except Exception,e:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION master2originUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(e)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    logfile.write('============================='+'\n')
    

def listBranches(wd,repo):
    path = wd + '/' + repo
    try:
        branches = Repo(path).git.branch('-r')
    except Exception:
        branches = ''
        if isfile(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
            with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                v\n')
                logfile.write('^                        ERROR OCCURRED                          v\n')
                logfile.write('^          IN FUNCTION listBranches in synchronizeGit.py         v\n')
                logfile.write('^                                                                v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write(str(Exception)+'\n')
                logfile.write('\n')
        else:
            with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
                logfile.write('\n')
                logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                logfile.write('^                                                                v\n')
                logfile.write('^                        ERROR OCCURRED                          v\n')
                logfile.write('^          IN FUNCTION listBranches in synchronizeGit.py         v\n')
                logfile.write('^                                                                v\n')
                logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                logfile.write('\n')
                logfile.write('                             DETAILS                             \n')
                logfile.write(str(Exception)+'\n')
                logfile.write('\n')
        sys.exc_clear()
    return branches

def origin2masterUpdate(wd,user):
    Git.USE_SHELL = True
    localrepos = listReposInWD(wd)
    if isfile(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log')):
        with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'a') as logfile:
            for repo in localrepos:
                path = wd + '/' + repo
                try:
                    currRepo = Repo(path)
                except Exception:
                    currRepo = ''
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
                    sys.exc_clear()
                '''
                print('')
                print('=============================')
                print(repo)
                print('')
                print(currRepo.git.status())
                '''
                logfile.write('\n')
                logfile.write('============================='+'\n')
                logfile.write(repo+'\n')
                logfile.write('\n'+'\n')
                try:
                    repoStatus = currRepo.git.status()
                    logfile.write(repoStatus+'\n')
                except Exception:
                    repoStatus = ''
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
                    sys.exc_clear()
                try:
                    isRepoDirty = currRepo.is_dirty()
                except Exception:
                    isRepoDirty = False
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
                    sys.exc_clear()
                if isRepoDirty or 'untracked files present' in repoStatus:
                    '''
                    print(repo + ' needs a push')
                    print('adding files ...')
                    '''
                    logfile.write(repo + ' needs a push'+'\n')
                    logfile.write('adding files ...'+'\n')
                    try:
                        currRepo.git.add('--all')
                        #print('...done. Committing with message:')
                        logfile.write('...done. Committing with message:'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                    try:
                        now = datetime.now()
                        commitMessage = 'committing changes on ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' at ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
                        #print(commitMessage)
                        logfile.write(commitMessage+'\n')
                        currRepo.git.commit(m=commitMessage)
                        #print('...done. Pushing changes to remote...')
                        logfile.write('...done. Pushing changes to remote...'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                    try:
                        currRepo.remotes.origin.push()
                        '''
                        print('...done.')
                        '''
                        logfile.write('...done.'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                    #print(currRepo.git.status())
                    try:
                        logfile.write(currRepo.git.status()+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                else:
                    #print(repo + ' is up-to-date')
                    try:
                        logfile.write(repo + ' is up-to-date'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    
                #print('=============================')
                logfile.write('=============================')
    else:
        with open(join(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'),'w') as logfile:
            for repo in localrepos:
                path = wd + '/' + repo
                try:
                    currRepo = Repo(path)
                except Exception:
                    currRepo = ''
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
                    sys.exc_clear()
                '''
                print('')
                print('=============================')
                print(repo)
                print('')
                print(currRepo.git.status())
                '''
                logfile.write('\n')
                logfile.write('============================='+'\n')
                logfile.write(repo+'\n')
                logfile.write('\n')
                try:
                    repoStatus = currRepo.git.status()
                    logfile.write(repoStatus+'\n')
                except Exception:
                    repoStatus = ''
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
                    sys.exc_clear()
                try:
                    isRepoDirty = currRepo.is_dirty()
                except Exception:
                    isRepoDirty = False
                    logfile.write('\n')
                    logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('^                        ERROR OCCURRED                          v\n')
                    logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                    logfile.write('^                                                                v\n')
                    logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    logfile.write('\n')
                    logfile.write('                             DETAILS                             \n')
                    logfile.write(str(Exception)+'\n')
                    logfile.write('\n')
                    sys.exc_clear()
                if isRepoDirty or 'untracked files present' in repoStatus:
                    '''
                    print(repo + ' needs a push')
                    print('adding files ...')
                    '''
                    logfile.write(repo + ' needs a push'+'\n')
                    logfile.write('adding files ...'+'\n')
                    try:
                        currRepo.git.add('--all')
                        #print('...done. Committing with message:')
                        logfile.write('...done. Committing with message:'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                    try:
                        now = datetime.now()
                        commitMessage = 'committing changes on ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' at ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
                        #print(commitMessage)
                        logfile.write(commitMessage+'\n')
                        currRepo.git.commit(m=commitMessage)
                        #print('...done. Pushing changes to remote...')
                        logfile.write('...done. Pushing changes to remote...'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                    try:
                        currRepo.remotes.origin.push()
                        '''
                        print('...done.')
                        '''
                        logfile.write('...done.'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                    #print(currRepo.git.status())
                    try:
                        logfile.write(currRepo.git.status()+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                else:
                    #print(repo + ' is up-to-date')
                    try:
                        logfile.write(repo + ' is up-to-date'+'\n')
                    except Exception:
                        logfile.write('\n')
                        logfile.write('>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('^                        ERROR OCCURRED                          v\n')
                        logfile.write('^     IN FUNCTION origin2masterUpdate in synchronizeGit.py       v\n')
                        logfile.write('^                                                                v\n')
                        logfile.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                        logfile.write('\n')
                        logfile.write('                             DETAILS                             \n')
                        logfile.write(str(Exception)+'\n')
                        logfile.write('\n')
                        sys.exc_clear()
                    
                #print('=============================')
                logfile.write('============================='+'\n')

'''

wd = 'C:/01_backup-folder/OneDrive/01_Luca/07_DocMASE/04_WD'

origin2masterUpdate(wd,user,pwd)
master2originUpdate(wd,user,pwd)
'''