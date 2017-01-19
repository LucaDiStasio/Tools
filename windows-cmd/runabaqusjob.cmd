SET abaquswd=2017-01-19_ABQfem_model00000000/abaqus
SET inputfile=../abqinp/2017-01-19_ABQfem_model00000000.inp
SET projectname=2017-01-19_ABQfem_model00000000
SET cpusnum=4

CD %abaquswd%

abaqus job=%projectname% analysis input=%inputfile% information=all interactive cpus=%cpusnum%
:: abaqus job=%projectname% analysis input=%inputfile% information=all background cpus=%cpusnum%

CD ..
CD ..
