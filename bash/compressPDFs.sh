#!/bin/bash

clear

PDFSETTINGS="/ebook"

NAMEVAR="_compressed"
EXT=".pdf"
declare -a FILESWITHOUTEXT=("Pole-emploi_Ouverture-droit-allocation_2017-03-29"
                            "Pole-emploi_Carte-demandeur-emploi_2017-04-04"
                            "Echographie_superficielle_2016-09-08"
                            "Lavot_echographie-abdominale_2017-04-28"
                            "Convocation_pour_hospitalisation_2016-04-13"
                            "etiquettes-hospitalisation_2016-04-13"
                            "Avis-arret-maladie_2016-11-02"
                            "Avis-arret-maladie_2016-12-22"
                            "Prudhommes-Metz_Convocation_2017-06-26"
                            "17_DI-STASIO_Avril_2017"
                            "18_DI-STASIO_Mai_2017"
                            "19_DI-STASIO_Juin_2017"
                            "2042_1950-complet-signe.pdf"
                            "Lavot_psychiatre_2016-10-17"
                            "Lavot_antidepressive_2016-10-15(1)"
                            )
                 
for f in ${FILESWITHOUTEXT[*]}; do
    INP="$f"
    OUT="$f"
    INP+="$EXT"
    OUT+="$NAMEVAR"
    OUT+="$EXT"
    echo $INP
    echo $OUT
    ps2pdf -dPDFSETTINGS=$PDFSETTINGS "$INP" "$OUT"
    okular "$OUT"
done