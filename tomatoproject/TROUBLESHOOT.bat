@echo off
REM ========================================
REM SmartCrop AI - Troubleshooting Tool
REM ========================================

:MENU
cls
echo.
echo ========================================
echo   SmartCrop AI - Troubleshooting
echo ========================================
echo.
echo What issue are you experiencing?
echo.
echo   1. Check Python installation
echo   2. Check virtual environment
echo   3. Check Django installation
echo   4. Check database
echo   5. Reset database (WARNING: Deletes all data!)
echo   6. Reinstall dependencies
echo   7. Check server port availability
echo   8. View system information
echo   9. Exit
echo.
set /p choice="Enter your choice (1-9): "

if "%choice%"=="1" goto CHECK_PYTHON
if "%choice%"=="2" goto CHECK_VENV
if "%choice%"=="3" goto CHECK_DJANGO
if "%choice%"=="4" goto CHECK_DB
if "%choice%"=="5" goto RESET_DB
if "%choice%"=="6" goto REINSTALL
if "%choice%"=="7" goto CHECK_PORT
if "%choice%"=="8" goto SYSTEM_INFO
if "%choice%"=="9" goto END

echo Invalid choice. Please try again.
timeout /t 2 >nul
goto MENU

:CHECK_PYTHON
cls
echo ========================================
echo Checking Python Installation...
echo ========================================
echo.
python --version
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please:
    echo   1. Download Python from python.org
    echo   2. Run installer
    echo   3. CHECK "Add Python to PATH"
    echo   4. Restart this script
) else (
    echo [OK] Python is installed correctly!
)
echo.
echo Checking pip...
pip --version
if errorlevel 1 (
    echo [ERROR] pip is not available!
) else (
    echo [OK] pip is installed correctly!
)
echo.
pause
goto MENU

:CHECK_VENV
cls
echo ========================================
echo Checking Virtual Environment...
echo ========================================
echo.
if exist "venv\Scripts\activate.bat" (
    echo [OK] Virtual environment exists!
    echo.
    echo Activating and checking Python path...
    call venv\Scripts\activate.bat
    where python
    echo.
    echo Installed packages:
    pip list
) else (
    echo [ERROR] Virtual environment not found!
    echo.
    echo To create it, run:
    echo   python -m venv venv
)
echo.
pause
goto MENU

:CHECK_DJANGO
cls
echo ========================================
echo Checking Django Installation...
echo ========================================
echo.
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    python -c "import django; print('Django version:', django.get_version())"
    if errorlevel 1 (
        echo [ERROR] Django is not installed!
        echo.
        echo To install, run:
        echo   pip install django
    ) else (
        echo [OK] Django is installed!
    )
) else (
    echo [ERROR] Virtual environment not found!
    echo Please create it first (Option 2)
)
echo.
pause
goto MENU

:CHECK_DB
cls
echo ========================================
echo Checking Database...
echo ========================================
echo.
if exist "db.sqlite3" (
    echo [OK] Database file exists!
    echo.
    echo Database size:
    dir db.sqlite3 | find "db.sqlite3"
    echo.
    echo Checking migrations...
    if exist "venv\Scripts\activate.bat" (
        call venv\Scripts\activate.bat
        python manage.py showmigrations
    )
) else (
    echo [WARNING] Database file not found!
    echo.
    echo To create it, run:
    echo   python manage.py migrate
)
echo.
pause
goto MENU

:RESET_DB
cls
echo ========================================
echo Reset Database
echo ========================================
echo.
echo WARNING: This will DELETE ALL DATA!
echo   - All predictions
echo   - All users
echo   - All admin accounts
echo.
set /p confirm="Are you sure? Type YES to confirm: "
if not "%confirm%"=="YES" (
    echo Cancelled.
    timeout /t 2 >nul
    goto MENU
)
echo.
echo Deleting database...
if exist "db.sqlite3" (
    del db.sqlite3
    echo [OK] Database deleted!
) else (
    echo [INFO] Database file not found.
)
echo.
echo Creating new database...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    python manage.py migrate
    echo.
    echo Creating superuser...
    python manage.py createsuperuser
) else (
    echo [ERROR] Virtual environment not found!
)
echo.
pause
goto MENU

:REINSTALL
cls
echo ========================================
echo Reinstall Dependencies
echo ========================================
echo.
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo Upgrading pip...
    python -m pip install --upgrade pip
    echo.
    echo Installing dependencies...
    pip install -r requirements.txt --upgrade
    echo.
    echo [OK] Dependencies reinstalled!
) else (
    echo [ERROR] Virtual environment not found!
)
echo.
pause
goto MENU

:CHECK_PORT
cls
echo ========================================
echo Checking Port 8000
echo ========================================
echo.
echo Checking if port 8000 is in use...
netstat -ano | findstr :8000
if errorlevel 1 (
    echo [OK] Port 8000 is available!
) else (
    echo [WARNING] Port 8000 is in use!
    echo.
    echo To kill the process:
    echo   1. Note the PID (last column above)
    echo   2. Run: taskkill /PID [number] /F
    echo.
    echo Or use a different port:
    echo   python manage.py runserver 8080
)
echo.
pause
goto MENU

:SYSTEM_INFO
cls
echo ========================================
echo System Information
echo ========================================
echo.
echo Windows Version:
ver
echo.
echo Python Version:
python --version 2>nul || echo Not found
echo.
echo pip Version:
pip --version 2>nul || echo Not found
echo.
echo Current Directory:
cd
echo.
echo Virtual Environment:
if exist "venv" (echo EXISTS) else (echo NOT FOUND)
echo.
echo Database:
if exist "db.sqlite3" (echo EXISTS) else (echo NOT FOUND)
echo.
echo Available Memory:
wmic OS get FreePhysicalMemory /Value
echo.
pause
goto MENU

:END
echo.
echo Exiting troubleshooting tool...
timeout /t 1 >nul
exit /b 0
