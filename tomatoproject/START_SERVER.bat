@echo off
REM ========================================
REM SmartCrop AI - Django Server Launcher
REM ========================================

echo.
echo ========================================
echo   SmartCrop AI - Starting Server
echo ========================================
echo.

REM Change to the script's directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run setup first:
    echo 1. Open Command Prompt in this folder
    echo 2. Run: python -m venv venv
    echo 3. Run: venv\Scripts\activate
    echo 4. Run: pip install -r requirements.txt
    echo 5. Run: python manage.py migrate
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if Django is installed
python -c "import django" 2>nul
if errorlevel 1 (
    echo [ERROR] Django is not installed!
    echo.
    echo Please install dependencies:
    echo   pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM Check if database exists
if not exist "db.sqlite3" (
    echo [WARNING] Database not found. Running migrations...
    python manage.py migrate
    echo.
    echo [INFO] Please create a superuser:
    python manage.py createsuperuser
)

REM Start the server
echo [2/3] Starting Django development server...
echo.
echo ========================================
echo   Server will start at:
echo   http://127.0.0.1:8000/
echo.
echo   Admin panel:
echo   http://127.0.0.1:8000/admin/
echo.
echo   Press CTRL+C to stop the server
echo ========================================
echo.

REM Run the server
python manage.py runserver

REM This runs when server is stopped
echo.
echo ========================================
echo   Server stopped
echo ========================================
echo.
pause
