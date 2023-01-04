@echo off & chcp 65001

:start
cls

echo Co chcesz zrobić?
echo 1 - Uruchom program
echo 2 - Informacje o projekcie
echo 3 - Backup
echo 4 - Wyjscie
echo Opcja:

set /p whatapp=

if %whatapp%==1 (
    goto 1
) else if %whatapp%==2 (
    goto 2
) else if %whatapp%==3 (
    goto 3
) else if %whatapp%==4 (
	goto 4
)

:1
python "main.py"
python "raport.py"
echo Skrypt został pomyślnie wykonany, otwieram wygenerowany raport...
"raport.html"
pause
goto start

:2
info.bat
goto start


:3
for /f %%a in ('powershell -Command "Get-Date -format yyyy_MM_dd__HH_mm_ss"') do set datetime=%%a
if not exist "Backups" mkdir Backups
cd Backups
mkdir "%datetime%"
cd %datetime%
mkdir input
mkdir output
cd ../
cd ../
xcopy /s input Backups\"%datetime%"\input
xcopy /s output Backups\"%datetime%"\output
xcopy styles.css Backups\"%datetime%"
xcopy raport.html Backups\"%datetime%"
echo Backup został pomyślnie wykonany, kliknij dowolny przycisk by powrócić do menu
pause
goto start

:4
echo Zakończono działanie programu, kliknij dowolny przycisk by wyłączyc okno
pause

