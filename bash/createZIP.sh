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

Zip files.

Tested in Ubuntu 14.04
'

DIR="annexes"

sudo rm -r $DIR

sudo mkdir $DIR

declare -a FILESWITHOUTEXT=("Pole-emploi_Ouverture-droit-allocation_2017-03-29_compressed.pdf" "Pole-emploi_Carte-demandeur-emploi_2017-04-04_compressed.pdf" "Echographie_superficielle_2016-09-08_compressed.pdf" "Lavot_echographie-abdominale_2017-04-28_compressed.pdf" "Convocation_pour_hospitalisation_2016-04-13_compressed.pdf" "etiquettes_hospitalisation_2016-04-13_compressed.pdf" "Avis-arret-maladie_2016-11-02_compressed.pdf" "Avis-arret-maladie_2016-12-22_compressed.pdf" "Prudhommes-Metz_Convocation_2017-06-26_compressed.pdf" "17_DI-STASIO_Avril_2017_compressed.pdf" "18_DI-STASIO_Mai_2017_compressed.pdf" "19_DI-STASIO_Juin_2017_compressed.pdf" "2042_1950-complet-signe_compressed.pdf" "Lavot_psychiatre_2016-10-17_compressed.pdf" "Lavot_antidepressive_2016-10-15(1)_compressed.pdf")

for f in ${FILESWITHOUTEXT[*]}; do
    INP="$f"
    OUT="$DIR"
    OUT+="/"
    OUT+="$f"
    echo "move ""$INP"" to ""$OUT"
    sudo cp $INP $OUT
done

gzip -v -r --best $DIR
