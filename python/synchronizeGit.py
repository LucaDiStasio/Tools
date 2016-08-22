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

import os
from datetime import datetime
from github import Github
from git import Git, Repo, InvalidGitRepositoryError

def listAllUserPublicRepos(user,pwd):
    repos = []
    g = Github(user,pwd)
    for repo in g.get_user().get_repos():
        repos.append(repo.name)
    return repos
    
def listDirsInWD(wd):
    dirs = []
    elements = os.listdir(wd)
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
    for repo in userrepos:
        if repo in localrepos:
            path = wd + '/' + repo
            untracked = Repo(path).untracked_files
            if not untracked:
                print repo + ' is up-to-date'
            else:
                print repo + ' needs a push'
        else:
            print repo + ' must be cloned'

def listBranches(wd,repo):
    path = wd + '/' + repo
    return Repo(path).git.branch('-r')

def origin2masterUpdate(wd,user,pwd):
    localrepos = listReposInWD(wd)
    for repo in localrepos:
        path = wd + '/' + repo
        currRepo = Repo(path)
        untracked = currRepo.untracked_files
        print ''
        print '============================='
        print repo
        print ''
        print currRepo.git.status()
        if not untracked:
            print repo + ' is up-to-date'
        else:
            print repo + ' needs a push'
            print 'adding files ...'
            currRepo.git.add('--all')
            print '...done. Committing with message:'
            now = datetime.now()
            commitMessage = 'committing changes on ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' at ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
            print commitMessage
            currRepo.git.commit(m=commitMessage)
            print '...done. Pushing changes to remote...'
            currRepo.remotes.origin.push()
            print '...done.'
            print currRepo.git.status()
        print '============================='


user = 'LucaDiStasio'
pwd = 'dylan666'

wd = 'C:/01_backup-folder/OneDrive/01_Luca/07_DocMASE/04_WD'

origin2masterUpdate(wd,user,pwd)
#master2originUpdate(wd,user,pwd)