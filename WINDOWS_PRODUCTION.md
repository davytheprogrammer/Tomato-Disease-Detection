# 🚀 Windows Production Deployment Guide

Complete guide to deploying SmartCrop AI on Windows Server for production use.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Server Preparation](#server-preparation)
3. [Production Setup](#production-setup)
4. [IIS Deployment](#iis-deployment)
5. [Waitress Deployment](#waitress-deployment)
6. [Windows Service Setup](#windows-service-setup)
7. [Database Configuration](#database-configuration)
8. [Security Hardening](#security-hardening)
9. [Monitoring & Logging](#monitoring--logging)
10. [Backup Strategy](#backup-strategy)

---

## Prerequisites

### Server Requirements
- **Windows Server 2016** or newer (2019/2022 recommended)
- **4GB RAM minimum** (8GB+ recommended)
- **20GB free disk space**
- **Static IP address** or domain name
- **Administrator access**

### Software Requirements
- Python 3.10 or 3.11
- PostgreSQL 14+ (recommended) or SQL Server
- IIS 10+ (if using IIS deployment)
- SSL certificate (for HTTPS)

---

## Server Preparation

### Step 1: Update Windows Server

```powershell
# Run Windows Update
Install-Module PSWindowsUpdate
Get-WindowsUpdate
Install-WindowsUpdate -AcceptAll -AutoReboot
```

### Step 2: Install Python

1. Download Python 3.10 or 3.11 from [python.org](https://www.python.org/downloads/windows/)
2. Run installer with these options:
   - ✅ Install for all users
   - ✅ Add Python to PATH
   - ✅ Install pip
3. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

### Step 3: Install PostgreSQL

1. Download from [postgresql.org](https://www.postgresql.org/download/windows/)
2. Install with default settings
3. Remember the postgres password
4. Add PostgreSQL to PATH:
   ```
   C:\Program Files\PostgreSQL\14\bin
   ```

### Step 4: Create Database

```cmd
# Login to PostgreSQL
psql -U postgres

# Create database and user
CREATE DATABASE smartcrop_ai;
CREATE USER smartcrop_user WITH PASSWORD 'your_secure_password';
ALTER ROLE smartcrop_user SET client_encoding TO 'utf8';
ALTER ROLE smartcrop_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE smartcrop_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE smartcrop_ai TO smartcrop_user;
\q
```

---

## Production Setup

### Step 1: Clone Project

```cmd
cd C:\inetpub\wwwroot
git clone <repository-url> smartcrop-ai
cd smartcrop-ai\tomatoproject
```

### Step 2: Create Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Production Dependencies

Create `requirements-production.txt`:
```txt
Django==4.2.7
tensorflow-cpu==2.13.0
Pillow==10.1.0
numpy==1.24.3
psycopg2-binary==2.9.9
gunicorn==21.2.0
whitenoise==6.6.0
waitress==2.1.2
python-dotenv==1.0.0
```

Install:
```cmd
pip install -r requirements-production.txt
```

### Step 4: Configure Environment

Create `.env` file:
```env
# Security
SECRET_KEY=your-very-long-random-secret-key-change-this-in-production
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,your-server-ip

# Database
DATABASE_URL=postgresql://smartcrop_user:your_secure_password@localhost:5432/smartcrop_ai

# Static/Media
STATIC_ROOT=C:/inetpub/wwwroot/smartcrop-ai/tomatoproject/staticfiles
MEDIA_ROOT=C:/inetpub/wwwroot/smartcrop-ai/tomatoproject/media

# Model Path
MODEL_PATH=C:/inetpub/wwwroot/smartcrop-ai/models/best_mobilenet_finetuned.keras
```

### Step 5: Update Django Settings

Edit `tomato_disease/settings.py`:

```python
import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

# Security
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
}

# Static files
STATIC_ROOT = os.getenv('STATIC_ROOT')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_ROOT = os.getenv('MEDIA_ROOT')
MEDIA_URL = '/media/'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

### Step 6: Run Migrations

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

## IIS Deployment

### Step 1: Install IIS

```powershell
# Install IIS with required features
Install-WindowsFeature -name Web-Server -IncludeManagementTools
Install-WindowsFeature -name Web-CGI
```

### Step 2: Install wfastcgi

```cmd
pip install wfastcgi
wfastcgi-enable
```

Note the output path (e.g., `C:\Python310\Scripts\wfastcgi-enable.exe`)

### Step 3: Create web.config

Create `web.config` in project root:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="Python FastCGI" 
           path="*" 
           verb="*" 
           modules="FastCgiModule" 
           scriptProcessor="C:\Python310\python.exe|C:\Python310\Scripts\wfastcgi.py" 
           resourceType="Unspecified" 
           requireAccess="Script" />
    </handlers>
    <staticContent>
      <mimeMap fileExtension=".keras" mimeType="application/octet-stream" />
    </staticContent>
  </system.webServer>
  <appSettings>
    <add key="PYTHONPATH" value="C:\inetpub\wwwroot\smartcrop-ai\tomatoproject" />
    <add key="WSGI_HANDLER" value="tomato_disease.wsgi.application" />
    <add key="DJANGO_SETTINGS_MODULE" value="tomato_disease.settings" />
  </appSettings>
</configuration>
```

### Step 4: Configure IIS Site

1. Open **IIS Manager**
2. Right-click **Sites** → **Add Website**
3. Configure:
   - **Site name:** SmartCrop AI
   - **Physical path:** `C:\inetpub\wwwroot\smartcrop-ai\tomatoproject`
   - **Binding:** HTTP, Port 80, your domain
4. Click **OK**

### Step 5: Set Permissions

```powershell
# Give IIS user permissions
icacls "C:\inetpub\wwwroot\smartcrop-ai" /grant "IIS_IUSRS:(OI)(CI)F" /T
icacls "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\media" /grant "IIS_IUSRS:(OI)(CI)F" /T
```

### Step 6: Configure SSL

1. Obtain SSL certificate (Let's Encrypt, commercial CA)
2. In IIS Manager, select your site
3. Click **Bindings** → **Add**
4. Select HTTPS, port 443, select certificate
5. Enable **Require SSL** in SSL Settings

---

## Waitress Deployment (Recommended)

Waitress is easier to set up than IIS and works great for production.

### Step 1: Install Waitress

```cmd
pip install waitress
```

### Step 2: Create Server Script

Create `run_waitress.py`:

```python
import os
from waitress import serve
from tomato_disease.wsgi import application

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f'Starting Waitress server on port {port}...')
    serve(
        application,
        host='0.0.0.0',
        port=port,
        threads=4,
        url_scheme='https',  # If behind reverse proxy with SSL
        channel_timeout=120,
        cleanup_interval=30,
        asyncore_use_poll=True
    )
```

### Step 3: Test Waitress

```cmd
python run_waitress.py
```

Access at: http://your-server-ip:8000/

---

## Windows Service Setup

Run Django as a Windows Service using NSSM.

### Step 1: Download NSSM

1. Download from [nssm.cc](https://nssm.cc/download)
2. Extract to `C:\nssm`
3. Add to PATH

### Step 2: Create Startup Script

Create `start_production.bat`:

```batch
@echo off
cd C:\inetpub\wwwroot\smartcrop-ai\tomatoproject
call venv\Scripts\activate.bat
python run_waitress.py
```

### Step 3: Install Service

```cmd
# Open Command Prompt as Administrator
nssm install SmartCropAI "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\start_production.bat"

# Configure service
nssm set SmartCropAI AppDirectory "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject"
nssm set SmartCropAI DisplayName "SmartCrop AI - Django Application"
nssm set SmartCropAI Description "AI-powered tomato disease detection system"
nssm set SmartCropAI Start SERVICE_AUTO_START

# Start service
nssm start SmartCropAI
```

### Step 4: Manage Service

```cmd
# Check status
nssm status SmartCropAI

# Stop service
nssm stop SmartCropAI

# Restart service
nssm restart SmartCropAI

# Remove service
nssm remove SmartCropAI confirm
```

---

## Database Configuration

### PostgreSQL Optimization

Edit `postgresql.conf`:

```ini
# Memory
shared_buffers = 256MB
effective_cache_size = 1GB
work_mem = 16MB

# Connections
max_connections = 100

# Performance
random_page_cost = 1.1
effective_io_concurrency = 200
```

Restart PostgreSQL:
```cmd
net stop postgresql-x64-14
net start postgresql-x64-14
```

### Automated Backups

Create `backup_database.bat`:

```batch
@echo off
set BACKUP_DIR=C:\Backups\SmartCropAI
set TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%
set BACKUP_FILE=%BACKUP_DIR%\smartcrop_ai_%TIMESTAMP%.sql

mkdir %BACKUP_DIR% 2>nul

"C:\Program Files\PostgreSQL\14\bin\pg_dump.exe" -U smartcrop_user -h localhost smartcrop_ai > %BACKUP_FILE%

echo Backup completed: %BACKUP_FILE%

# Delete backups older than 30 days
forfiles /p %BACKUP_DIR% /m *.sql /d -30 /c "cmd /c del @path"
```

Schedule with Task Scheduler:
```cmd
schtasks /create /tn "SmartCrop AI Backup" /tr "C:\inetpub\wwwroot\smartcrop-ai\backup_database.bat" /sc daily /st 02:00
```

---

## Security Hardening

### Step 1: Firewall Configuration

```powershell
# Allow HTTP/HTTPS
New-NetFirewallRule -DisplayName "SmartCrop AI HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
New-NetFirewallRule -DisplayName "SmartCrop AI HTTPS" -Direction Inbound -Protocol TCP -LocalPort 443 -Action Allow

# Block direct access to Django port
New-NetFirewallRule -DisplayName "Block Django Port" -Direction Inbound -Protocol TCP -LocalPort 8000 -Action Block
```

### Step 2: File Permissions

```powershell
# Restrict access to sensitive files
icacls "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\.env" /inheritance:r /grant:r "Administrators:F"
icacls "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\db.sqlite3" /inheritance:r /grant:r "IIS_IUSRS:F" /grant:r "Administrators:F"
```

### Step 3: Regular Updates

Create `update_system.bat`:

```batch
@echo off
echo Updating Python packages...
cd C:\inetpub\wwwroot\smartcrop-ai\tomatoproject
call venv\Scripts\activate.bat
pip list --outdated
pip install --upgrade pip
echo.
echo Review outdated packages and update as needed
pause
```

---

## Monitoring & Logging

### Step 1: Configure Django Logging

Add to `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'maxBytes': 1024 * 1024 * 10,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'errors.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'error_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Step 2: Monitor Service

Create `monitor_service.ps1`:

```powershell
$serviceName = "SmartCropAI"
$service = Get-Service -Name $serviceName -ErrorAction SilentlyContinue

if ($service.Status -ne 'Running') {
    Start-Service -Name $serviceName
    $message = "Service $serviceName was down and has been restarted at $(Get-Date)"
    Write-EventLog -LogName Application -Source "SmartCrop AI" -EventId 1001 -Message $message
    # Send email notification (configure SMTP)
}
```

Schedule to run every 5 minutes.

---

## Backup Strategy

### Full Backup Script

Create `full_backup.bat`:

```batch
@echo off
set BACKUP_ROOT=D:\Backups\SmartCropAI
set TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%
set BACKUP_DIR=%BACKUP_ROOT%\%TIMESTAMP%

mkdir %BACKUP_DIR%

echo Backing up database...
"C:\Program Files\PostgreSQL\14\bin\pg_dump.exe" -U smartcrop_user smartcrop_ai > %BACKUP_DIR%\database.sql

echo Backing up media files...
xcopy /E /I /Y "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\media" "%BACKUP_DIR%\media"

echo Backing up configuration...
copy "C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\.env" "%BACKUP_DIR%\.env"

echo Backup completed: %BACKUP_DIR%
```

---

## Production Checklist

- [ ] Python 3.10+ installed
- [ ] PostgreSQL installed and configured
- [ ] Virtual environment created
- [ ] Production dependencies installed
- [ ] `.env` file configured with production settings
- [ ] `DEBUG=False` in settings
- [ ] Strong `SECRET_KEY` generated
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] Superuser created
- [ ] SSL certificate installed
- [ ] Firewall rules configured
- [ ] File permissions set correctly
- [ ] Windows Service installed (NSSM)
- [ ] Service starts automatically
- [ ] Logging configured
- [ ] Backup script scheduled
- [ ] Monitoring in place
- [ ] Application tested thoroughly

---

## Useful Commands

```cmd
# Check service status
sc query SmartCropAI

# View service logs
nssm dump SmartCropAI

# Restart PostgreSQL
net stop postgresql-x64-14
net start postgresql-x64-14

# View Django logs
type C:\inetpub\wwwroot\smartcrop-ai\tomatoproject\logs\django.log

# Check port usage
netstat -ano | findstr :8000

# Test database connection
psql -U smartcrop_user -d smartcrop_ai -h localhost
```

---

**SmartCrop AI** - Production Deployment on Windows Server  
*Last Updated: December 2024*
