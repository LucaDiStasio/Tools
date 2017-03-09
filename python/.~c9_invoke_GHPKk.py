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
from os import remove, chdir
from os.path import isfile, join
from datetime import datetime
from github import Github
from git import Git, Repo, InvalidGitRepositoryError
from time import strftime
from platform import system
import subprocess

def logSuccessMessage(wd,logfile,message):
    if isfile(join(wd,logfile)):
        with open(join(wd,logfile),'a') as log:
            log.write(message + '\n')
    else:
        with open(join(wd,logfile),'w') as log:
            log.write('\n')
            log.write(message + '\n')
            
def logErrorMessage(wd,logfile,function,library,error):
    if isfile(join(wd,logfile)):
        with open(join(wd,logfile),'a') as log:
            log.write('\n')
            log.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
            log.write('^                                                                v\n')
            log.write('^                        ERROR OCCURRED                          v\n')
            log.write('^     IN FUNCTION ' + function + ' in ' + library + '       v\n')
            log.write('^                                                                v\n')
            log.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
            log.write('\n')
            log.write('                             DETAILS                             \n')
            log.write('\n')
            log.write(str(error)+'\n')
            log.write('\n')
    else:
        with open(join(wd,logfile),'w') as log:
            log.write('\n')
            log.write('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
            log.write('^                                                                v\n')
            log.write('^                        ERROR OCCURRED                          v\n')
            log.write('^     IN FUNCTION ' + function + ' in ' + library + '       v\n')
            log.write('^                                                                v\n')
            log.write('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
            log.write('\n')
            log.write('                             DETAILS                             \n')
            log.write('\n')
            log.write(str(error)+'\n')
            log.write('\n')

def clearFile(wd,file):
    logfilename = datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'
    logSuccessMessage(wd,logfilename,'Executing file clearing...')
    try:
        remove(join(wd,file))
        logSuccessMessage(wd,logfilename,'...done.')
    except Exception,e:
        logErrorMessage(wd,logfilename,'clearFile','synchronizeGit.py',e)

def changeOrigin(mode,wd,user,pwd,repo):
    # mode 1: public to secure
    #      2: secure to public
    logfilename = datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'
    if system() is 'Linux':
        chdir(join(wd,repo))
        logSuccessMessage(wd,logfilename,'Checking current remote url...')
        p=subprocess.Popen('git remote show origin',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout,stderr=p.communicate()
        if len(stdout.replace(' ',''))>0:
            logSuccessMessage(wd,logfilename,stdout)
        if len(stderr.replace(' ',''))>0:
            logErrorMessage(wd,logfilename,'changeOrigin','synchronizeGit.py',stderr)
        chdir(wd)
        logSuccessMessage(wd,logfilename,'...done.')
    if mode is 1:
        logSuccessMessage(wd,logfilename,'Changing remote url of repo ' + repo + ' from public to secure...')
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
            cli.write('cd ' + join(wd,repo) + '\n')
            cli.write('\n')
            cli.write('git remote set-url origin https://' + user + ':' + pwd + '@github.com/' + user + '/' + repo + '.git\n')
        try:
            if system() is 'Windows':
                subprocess.call('cmd.exe /C ' + changeUrlFilePath,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            elif system() is 'Linux':
                chdir(join(wd,repo))
                p=subprocess.Popen('sudo git remote set-url origin https://' + user + ':' + pwd + '@github.com/' + user + '/' + repo + '.git',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                stdout,stderr=p.communicate()
                if len(stdout.replace(' ',''))>0:
                    logSuccessMessage(wd,logfilename,stdout)
                if len(stderr.replace(' ',''))>0:
                    logErrorMessage(wd,logfilename,'changeOrigin','synchronizeGit.py',stderr)
                chdir(wd)
            logSuccessMessage(wd,logfilename,'...done.')
        except Exception,e:
            logErrorMessage(wd,logfilename,'changeOrigin','synchronizeGit.py',e)
        clearFile(wd,changeUrlFilePath)
    elif mode is 2:
        logSuccessMessage(wd,logfilename,'Changing remote url of repo ' + repo + ' from secure to public...')
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
            cli.write('cd ' + join(wd,repo) + '\n')
            cli.write('\n')
            cli.write('git remote set-url origin https://github.com/' + user + '/' + repo + '\n')
        try:
            if system() is 'Windows':
                subprocess.call('cmd.exe /C ' + changeUrlFilePath,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            elif system() is 'Linux':
                chdir(join(wd,repo))
                p=subprocess.Popen('sudo git remote set-url origin https://github.com/' + user + '/' + repo,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                stdout,stderr=p.communicate()
                if len(stdout.replace(' ',''))>0:
                    logSuccessMessage(wd,logfilename,stdout)
                if len(stderr.replace(' ',''))>0:
                    logErrorMessage(wd,logfilename,'changeOrigin','synchronizeGit.py',stderr)
                chdir(wd)
            logSuccessMessage(wd,logfilename,'...done.')
        except Exception,e:
            logErrorMessage(wd,logfilename,'changeOrigin','synchronizeGit.py',e)
        clearFile(wd,changeUrlFilePath)
    else:
        logSuccessMessage(wd,logfilename,'Tried to change Git origin but no mode provided. Leaving unchanged.')
    if system() is 'Linux':
        logSuccessMessage(wd,logfilename,'Checking current remote url...')
        chdir(join(wd,repo))
        p=subprocess.Popen('git remote show origin',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout,stderr=p.communicate()
        if len(stdout.replace(' ',''))>0:
            logSuccessMessage(wd,logfilename,stdout)
        if len(stderr.replace(' ',''))>0:
            logErrorMessage(wd,logfilename,'changeOrigin','synchronizeGit.py',stderr)
        chdir(wd)
        logSuccessMessage(wd,logfilename,'...done.')

def listAllUserPublicRepos(user,pwd,wd):
    repos = []
    g = Github(user,pwd)
    for repo in g.get_user().get_repos():
        try:
            repos.append(repo.name)
        except Exception,e:
            logErrorMessage(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log','listAllUserPublicRepos','synchronizeGit.py',e)
            sys.exc_clear()
    return repos
    
def listDirsInWD(wd):
    dirs = []
    try:
        elements = os.listdir(wd)
    except Exception,e:
        elements = []
        logErrorMessage(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log','listDirsInWD','synchronizeGit.py',e)
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
        logErrorMessage(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log','checkIfDirIsRepo','synchronizeGit.py',InvalidGitRepositoryError)
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
    userrepos = listAllUserPublicRepos(user,pwd,wd)
    localrepos = listReposInWD(wd)
    logfilename = datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'
    for repo in userrepos:
        if repo in localrepos:
            logSuccessMessage(wd,logfilename,'=============================')
            logSuccessMessage(wd,logfilename,repo)
            changeOrigin(1,wd,user,pwd,repo)
            logSuccessMessage(wd,logfilename,'Pulling...')
            path = wd + '/' + repo
            try:
                currRepo = Repo(path)
            except Exception,e:
                currRepo = ''
                logErrorMessage(wd,logfilename,'master2originUpdate','synchronizeGit.py',e)
                sys.exc_clear()
            try:
                currRepo.remotes.origin.pull()
            except Exception,e:
                logErrorMessage(wd,logfilename,'master2originUpdate','synchronizeGit.py',e)
                sys.exc_clear()
            logSuccessMessage(wd,logfilename,'...done.')
            try:
                logSuccessMessage(wd,logfilename,currRepo.git.status())
            except Exception,e:
                logErrorMessage(wd,logfilename,'master2originUpdate','synchronizeGit.py',e)
                sys.exc_clear()
            changeOrigin(2,wd,user,pwd,repo)
            logSuccessMessage(wd,logfilename,'============================='+'\n')
        else:
            logSuccessMessage(wd,logfilename,'=============================')
            logSuccessMessage(wd,logfilename,repo)
            logSuccessMessage(wd,logfilename,'Cloning...')
            try:
                remote = 'https://' + user + ':' + pwd + '@github.com/' + user + '/' + repo + '.git'
                local = wd + '/' + repo
                currRepo = Repo.clone_from(remote, local)
            except Exception,e:
                logErrorMessage(wd,logfilename,'master2originUpdate','synchronizeGit.py',e)
                logSuccessMessage(wd,logfilename,'Trying to execute from command line...')
                sys.exc_clear()
                cloneRepoFile = 'cloneRepoFile'
                if system() is 'Windows':
                    cloneRepoFile += '.cmd'
                elif system() is 'Linux':
                    cloneRepoFile += '.sh'
                cloneRepoFilePath = join(wd,cloneRepoFile)
                with open(cloneRepoFilePath,'w') as cli:
                    if system() is 'Linux':
                        logSuccessMessage(wd,logfilename,'Writing Linux bash file')
                        cli.write('#!/bin/bash\n')
                        cli.write('\n')
                    else:
                        logSuccessMessage(wd,logfilename,'Writing Windows command file')
                    cli.write('cd ' + wd + '\n')
                    cli.write('\n')
                    cli.write('git clone https://' + user + ':' + pwd + '@github.com/' + user + '/' + repo + '.git\n')
                try:
                    if system() is 'Windows':
                        logSuccessMessage(wd,logfilename,'Executing Windows command file')
                        subprocess.call('cmd.exe /C ' + cloneRepoFilePath,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    elif system() is 'Linux':
                        logSuccessMessage(wd,logfilename,'Executing Linux bash file')
                        subprocess.call('chmod a+x ' + cloneRepoFilePath,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                        subprocess.call('./' + cloneRepoFile,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    logSuccessMessage(wd,logfilename,'Done.')
                except Exception,e:
                    logErrorMessage(wd,logfilename,'master2originUpdate','synchronizeGit.py',e)
                clearFile(wd,cloneRepoFilePath)
            logSuccessMessage(wd,logfilename,'...done.')
            changeOrigin(2,wd,user,pwd,repo)
            try:
                logSuccessMessage(wd,logfilename,currRepo.git.status())
            except Exception,e:
                logErrorMessage(wd,logfilename,'master2originUpdate','synchronizeGit.py',e)     
                sys.exc_clear()
            logSuccessMessage(wd,logfilename,'=============================')
    

def listBranches(wd,repo):
    path = wd + '/' + repo
    try:
        branches = Repo(path).git.branch('-r')
    except Exception:
        branches = ''
        logErrorMessage(wd,datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log','listBranches','synchronizeGit.py',e)
        sys.exc_clear()
    return branches

def origin2masterUpdate(wd,user,pwd):
    logfilename = datetime.now().strftime('%Y-%m-%d_%H-00-00')+'_initWD.log'
    if system() is 'Windows':
        Git.USE_SHELL = True
    elif system() is 'Linux':
        Git.USE_SHELL = False
    localrepos = listReposInWD(wd)
    for repo in localrepos:
        path = wd + '/' + repo
        changeOrigin(1,wd,user,pwd,repo)
        try:
            currRepo = Repo(path)
        except Exception,e:
            currRepo = ''
            logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
            sys.exc_clear()
        logSuccessMessage(wd,logfilename,'=============================')
        logSuccessMessage(wd,logfilename,repo)
        try:
            repoStatus = currRepo.git.status()
            logSuccessMessage(wd,logfilename,repoStatus)
        except Exception,e:
            repoStatus = ''
            logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
            sys.exc_clear()
        try:
            isRepoDirty = currRepo.is_dirty()
        except Exception,e:
            isRepoDirty = False
            logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
            sys.exc_clear()
        if isRepoDirty or 'untracked files present' in repoStatus:
            logSuccessMessage(wd,logfilename,repo + ' needs a push')
            changeOrigin(1,wd,user,pwd,repo)
            logSuccessMessage(wd,logfilename,'adding files ...')
            try:
                currRepo.git.add('--all')
                logSuccessMessage(wd,logfilename,'...done. Committing with message:')
            except Exception,e:
                logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
            try:
                now = datetime.now()
                commitMessage = 'committing changes on ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' at ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
                logSuccessMessage(wd,logfilename,commitMessage)
                currRepo.git.commit(m=commitMessage)
                logSuccessMessage(wd,logfilename,'...done. Pushing changes to remote...')
            except Exception,e:
                logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
            try:
                currRepo.remotes.origin.push()
                logSuccessMessage(wd,logfilename,'...done.')
            except Exception,e:
                logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
            try:
                logSuccessMessage(wd,logfilename,currRepo.git.status())
            except Exception,e:
                logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
                sys.exc_clear()
        else:
            try:
                logSuccessMessage(wd,logfilename,repo + ' is up-to-date')
            except Exception,e:
                logErrorMessage(wd,logfilename,'origin2masterUpdate','synchronizeGit.py',e)
                sys.exc_clear()
        changeOrigin(2,wd,user,pwd,repo)
        logSuccessMessage(wd,logfilename,'=============================')
