setlocal

rem Find the activate.bat file and set its path to a variable
for /R %%a in (activate.bat) do (
  if exist "%%a" set "activate_path=%%a"
)

rem Find the python.exe file and set its path to a variable
for /R %%b in (python.exe) do (
  if exist "%%b" set "python_path=%%b"
)

rem Find the stay_awake.py file and set its path to a variable
for /R %%c in (stay_awake.py) do (
  if exist "%%c" set "script_path=%%c"
)

rem Run the commands using the variables
"%activate_path%" ^
&& "%python_path%" -u "%script_path%"
pause
