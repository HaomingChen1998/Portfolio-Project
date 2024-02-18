@echo off

 call :isAdmin

 if %errorlevel% == 0 (
    goto :run
 ) else (
    echo Requesting administrative privileges...
    goto :UACPrompt
 )

 exit /b

 :isAdmin
    fsutil dirty query %systemdrive% >nul
 exit /b

 :run
setlocal

rem Set the base directory to the directory of the batch file
set "base_dir=%~dp0"

rem Find the activate.bat file and set its path to a variable
for /R "%base_dir%" %%a in (activate.bat) do (
  if exist "%%a" set "activate_path=%%a"
)

rem Find the python.exe file and set its path to a variable
for /R "%base_dir%" %%b in (python.exe) do (
  if exist "%%b" set "python_path=%%b"
)

rem Find the stay_awake.py file and set its path to a variable
for /R "%base_dir%" %%c in (stay_awake.py) do (
  if exist "%%c" set "script_path=%%c"
)

rem Run the commands using the variables
"%activate_path%" ^
&& "%python_path%" -u "%script_path%"
pause
 exit /b

 :UACPrompt
   echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
   echo UAC.ShellExecute "cmd.exe", "/c %~s0 %~1", "", "runas", 1 >> "%temp%\getadmin.vbs"

   "%temp%\getadmin.vbs"
   del "%temp%\getadmin.vbs"
  exit /B`