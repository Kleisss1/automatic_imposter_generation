@echo off
echo Welcome to the .vmd imposter generation script by Kleis.
echo.
set current_dir=%cd%
echo Your current .py script directory is:
echo.
echo %current_dir%  
echo.

echo If it isn't correct, please set the directory in your .bat file (open the bat file with any editor of your liking). &REM If you want to change the directory, go to the sixth line. Where it says current_dir=%cd%, replace %cd% with the directory where the script sits.

echo. 

echo Press any key to generate VMD files.

echo.

pause >nul

	vmd_script.py 
	
	echo.

echo Press any key to exit the program.
pause >nul
exit



