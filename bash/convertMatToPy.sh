#!/bin/bash

: '
=====================================================================================

Copyright (c) 2016 - 2017 Luca Di Stasio
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

Convert Matlab/Octave source code to Python Numpy/Scipy.

Tested in Ubuntu 14.04
'

function joinBy {
  local IFS="$1"; shift; echo "$*";
}

function readContentDir {
  for content in $1/*
  do
    if [ -d $content ]
    then
      echo "In directory "$content
      readContentDir $content
    elif [[ -f $content && ${content: -2} == ".m" && "$content" != *"ABQ"* ]]
    then
      IFS='/' read -a path <<< "$content"
      echo "Matlab .m file "${path[-1]}" in repo "${path[4]}", folder "${path[5]}
      replaceWith="python"
      pyExt=".py"
      localPython=${content//.m/$pyExt}
      pythonContent=${content//matlab/$replaceWith}
      IFS='/' read -a pythonFilePath <<< "$pythonContent"
      IFS='/' read -a localPythonFilePath <<< "$localPython"
      pythonPath="${pythonFilePath[0]}"
      for i in "${!pythonFilePath[@]}"; do
        if [[ $i >  0 && $i -lt $(( ${#pythonFilePath[@]}-1 )) ]]; then
          pythonPath=$pythonPath"/"${pythonFilePath[$i]}
        fi
      done
      echo "File will be translated in local file "$localPython
      sudo python /home/luca/libermate/libermate.py $content
      echo "Translation completed"
      echo "Python folder to be created if it does not exist: "$pythonPath
      sudo mkdir -p $pythonPath
      echo "Python folder created"
      newPythonFile=$pythonPath"/"${localPythonFilePath[-1]}
      echo "File will then be copied to "$newPythonFile
      sudo cp $localPython $newPythonFile
      echo "File "$localPython" will be removed"
      sudo rm $localPython
      echo "File removed"
    fi
  done
}

WD=$1

echo "Working directory to be analyzed: "$WD

readContentDir $WD
