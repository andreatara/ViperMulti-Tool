@echo off
chcp 65001 > nul
cls
echo
echo ██╗   ██╗██╗██████╗ ███████╗██████╗ 
echo ██║   ██║██║██╔══██╗██╔════╝██╔══██╗
echo ██║   ██║██║██████╔╝█████╗  ██████╔╝
echo ╚██╗ ██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗
echo  ╚████╔╝ ██║██║     ███████╗██║  ██║
echo   ╚═══╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
echo.
echo ~~by Tara
echo.
echo Installing dependencies in 3 seconds...
timeout /t 3 /nobreak > nul
pip3 install -r requirements.txt
echo.
timeout /t 1 /nobreak > nul
echo.
echo Done..!
echo.
echo Building Viper to a single executable in 3 seconds...
timeout /t 3 /nobreak > nul
python -m PyInstaller --onefile Viper.py
echo.
echo Done..!
echo Your Viper executable is located in the 'dist' folder. You can now move it to your desired location.
echo.
echo OR you can start Viper with python by typing 'python Viper.py' in the terminal.

set /p "input=Start Viper now? (y/n) -> "
if /i "%input%"=="y" (
    echo Starting Viper...
    timeout /t 1 /nobreak > nul
    start dist\Viper.exe
) else (
    echo Exiting...
    timeout /t 1 /nobreak > nul
)
exit