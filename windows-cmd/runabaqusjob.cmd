SET date=%1
SET number=%2
SET abaquswd=%date%_ABQfem_model%number%/abaqus
SET inputfile=../abqinp/%date%_ABQfem_model%number%.inp
SET projectname=%date%_ABQfem_model%number%
SET cpusnum=4

CD %abaquswd%

abaqus job=%projectname% analysis input=%inputfile% information=all interactive cpus=%cpusnum%
:: abaqus job=%projectname% analysis input=%inputfile% information=all background cpus=%cpusnum%

CD ..
CD ..
