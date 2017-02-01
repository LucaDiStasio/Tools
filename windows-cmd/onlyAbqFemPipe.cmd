SET pyfolder=D:\OneDrive\01_Luca\07_DocMASE\06_WD\thin_ply_mechanics\python
SET pyexec=runAbaqus
SET inputdeck=2017-01-31_AbaqusInputDeck
SET inputdir=D:\01_Luca\07_Data\03_FEM
SET workdir=D:\01_Luca\07_Data\03_FEM
SET statusfile=2017-01-26_AbaqusParametricRun_2017-01-31_14-57-39

python %pyfolder%/%pyexec%.py -i %inputdeck%.csv -d %inputdir% -w %workdir% -s %statusfile%.sta
