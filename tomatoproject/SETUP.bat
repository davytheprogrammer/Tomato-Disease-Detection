@echo off
REM ========================================
REM SmartCrop AI - Initial Setup Script
REM ========================================

echo.
echo ========================================
echo   SmartCrop AI - Initial Setup
echo ========================================
echo.
echo This script will:
echo   1. Create virtual environment
echo   2. Install dependencies
echo   3. Run database migrations
echo   4. Collect static files
echo   5. Create admin user
echo.
echo This may take 5-10 minutes...
echo.
pause

REM Change to the script's directory
cd /d "%~dp0"

REM Step 1: Create virtual environment
echo.
echo ========================================
echo [1/5] Creating virtual environment...
echo ========================================
if exist "venv" (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment!
        echo Make sure Python is installed and added to PATH.
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)

REM Step 2: Activate and install dependencies
echo.
echo ========================================
echo [2/5] Installing dependencies...
echo ========================================
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)
echo Dependencies installed successfully!

REM Step 3: Run migrations
echo.
echo ========================================
echo [3/5] Setting up database...
echo ========================================
python manage.py makemigrations
python manage.py migrate
if errorlevel 1 (
    echo [ERROR] Failed to run migrations!
    pause
    exit /b 1
)
echo Database setup complete!

REM Step 4: Collect static files
echo.
echo ========================================
echo [4/5] Collecting static files...
echo ========================================
python manage.py collectstatic --noinput
if errorlevel 1 (
    echo [WARNING] Failed to collect static files.
    echo This is not critical for development.
)
echo Static files collected!

REM Step 5: Create superuser
echo.
echo ========================================
echo [5/5] Creating admin user...
echo ========================================
echo.
echo Please enter admin credentials:
python manage.py createsuperuser

REM Final message
echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo You can now start the server by:
echo   1. Double-clicking START_SERVER.bat
echo   OR
echo   2. Running: python manage.py runserver
echo.
echo Access the application at:
echo   http://127.0.0.1:8000/
echo.
echo Admin panel:
echo   http://127.0.0.1:8000/admin/
echo.
pause
