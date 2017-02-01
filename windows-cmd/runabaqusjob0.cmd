SET wd=D:\01_Luca\07_Data\03_FEM
SET projectname=2017-01-31_ABQfem_model00000211
SET cpusnum=8
SET runmode=background
SET abaquswd=%wd%\%projectname%\abaqus
SET inputfile=%wd%\%projectname%\abqinp\%projectname%.inp

CD %abaquswd%

abaqus job=%projectname% analysis input=%inputfile% information=all %runmode% cpus=%cpusnum%
