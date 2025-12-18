# 🪟 SmartCrop AI - Complete Windows Setup Guide

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2%2B-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange)
![Windows](https://img.shields.io/badge/Windows-10%2F11-blue)

**Complete step-by-step guide to set up and run the Tomato Disease Detection Django application on Windows.**

---

## 📋 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Initial Setup](#-initial-setup)
3. [Python Installation](#-python-installation)
4. [Project Setup](#-project-setup)
5. [Virtual Environment](#-virtual-environment)
6. [Dependencies Installation](#-dependencies-installation)
7. [Database Setup](#-database-setup)
8. [Static Files Configuration](#-static-files-configuration)
9. [Running the Application](#-running-the-application)
10. [Troubleshooting](#-troubleshooting)
11. [Production Deployment](#-production-deployment)
12. [Additional Resources](#-additional-resources)

**📘 For production deployment on Windows Server, see [WINDOWS_PRODUCTION.md](WINDOWS_PRODUCTION.md)**

---

## 🎯 Prerequisites

Before starting, ensure you have:

- **Windows 10 or Windows 11** (64-bit)
- **Administrator access** to install software
- **At least 4GB RAM** (8GB recommended)
- **5GB free disk space**
- **Stable internet connection** for downloading packages
- **Modern web browser** (Chrome, Firefox, or Edge)

---

## 🚀 Initial Setup

### Step 1: Check Your Windows Version

1. Press `Win + R`
2. Type `winver` and press Enter
3. Ensure you're running Windows 10 (build 1909+) or Windows 11

### Step 2: Enable Long Path Support (Important!)

Django projects can have deep directory structures. Enable long paths:

1. Press `Win + R`, type `gpedit.msc`, press Enter
2. Navigate to: **Computer Configuration** → **Administrative Templates** → **System** → **Filesystem**
3. Double-click **Enable Win32 long paths**
4. Select **Enabled**, click **OK**

**Alternative method (PowerShell as Admin):**
```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

---

## 🐍 Python Installation

### Step 1: Download Python

1. Visit [python.org/downloads](https://www.python.org/downloads/)
2. Download **Python 3.10.x** or **Python 3.11.x** (64-bit)
3. **Important:** Python 3.12+ may have compatibility issues with TensorFlow

### Step 2: Install Python

1. Run the downloaded installer
2. ✅ **CHECK "Add Python to PATH"** (CRITICAL!)
3. Click **"Customize installation"**
4. Ensure these are checked:
   - ✅ pip
   - ✅ py launcher
   - ✅ for all users (requires admin)
5. Click **Next**
6. Advanced Options - Check:
   - ✅ Install for all users
   - ✅ Add Python to environment variables
   - ✅ Precompile standard library
7. Set installation path: `C:\Python310` (easier to manage)
8. Click **Install**

### Step 3: Verify Installation

Open **Command Prompt** (Win + R → `cmd`) and run:

```cmd
python --version
```
**Expected output:** `Python 3.10.x` or `Python 3.11.x`

```cmd
pip --version
```
**Expected output:** `pip 23.x.x from C:\Python310\lib\site-packages\pip (python 3.10)`

**If Python is not recognized:**
1. Search for "Environment Variables" in Windows Search
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "System variables", find "Path"
5. Click "Edit" → "New"
6. Add: `C:\Python310` and `C:\Python310\Scripts`
7. Click OK, restart Command Prompt

---

## 📁 Project Setup

### Step 1: Download the Project

**Option A: Using Git**

1. Install Git for Windows from [git-scm.com](https://git-scm.com/download/win)
2. Open Command Prompt
3. Navigate to your desired location:
   ```cmd
   cd C:\Users\YourUsername\Documents
   ```
4. Clone the repository:
   ```cmd
   git clone <repository-url>
   cd Tomato_Disease_Detection-main
   ```

**Option B: Download ZIP**

1. Download the project ZIP file
2. Extract to: `C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main`
3. Open Command Prompt and navigate:
   ```cmd
   cd C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main
   ```

### Step 2: Navigate to Django Project

```cmd
cd tomatoproject
```

Your current directory should now be:
```
C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject
```

---

## 🔧 Virtual Environment

### Why Use a Virtual Environment?

- Isolates project dependencies
- Prevents conflicts with other Python projects
- Makes deployment easier
- Keeps your system Python clean

### Step 1: Create Virtual Environment

```cmd
python -m venv venv
```

This creates a `venv` folder in your project directory.

### Step 2: Activate Virtual Environment

```cmd
venv\Scripts\activate
```

**Success indicator:** Your command prompt should now show `(venv)` at the beginning:
```
(venv) C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject>
```

**Troubleshooting Activation Issues:**

If you get an error about execution policies:

1. Open **PowerShell as Administrator**
2. Run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Type `Y` and press Enter
4. Close PowerShell, return to Command Prompt
5. Try activating again

**Alternative activation (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

### Step 3: Verify Virtual Environment

```cmd
where python
```

Should show: `C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject\venv\Scripts\python.exe`

---

## 📦 Dependencies Installation

### Step 1: Upgrade pip

```cmd
python -m pip install --upgrade pip
```

### Step 2: Install Project Dependencies

```cmd
pip install -r requirements.txt
```

This installs:
- Django 4.2+
- TensorFlow 2.13+
- Pillow (image processing)
- NumPy
- Other required packages

**Installation may take 5-10 minutes** depending on your internet speed.

### Step 3: Verify Installation

```cmd
pip list
```

Check that these packages are installed:
- Django
- tensorflow
- Pillow
- numpy
- gunicorn (may fail on Windows, that's OK for development)

**If TensorFlow installation fails:**

Try installing a specific version:
```cmd
pip install tensorflow==2.13.0
```

Or use CPU-only version:
```cmd
pip install tensorflow-cpu==2.13.0
```

---

## 🗄️ Database Setup

### Step 1: Understand Django Migrations

Django uses migrations to create and update database tables. Think of migrations as version control for your database schema.

### Step 2: Create Migration Files

```cmd
python manage.py makemigrations
```

**Expected output:**
```
Migrations for 'tomato_app':
  tomato_app\migrations\0001_initial.py
    - Create model Prediction
    - Create model Disease
```

**If you see "No changes detected":** That's fine, migrations already exist.

### Step 3: Apply Migrations

```cmd
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tomato_app
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  ...
  Applying tomato_app.0001_initial... OK
```

This creates a `db.sqlite3` file in your project directory.

### Step 4: Create Superuser (Admin Account)

```cmd
python manage.py createsuperuser
```

You'll be prompted for:
- **Username:** (e.g., `admin`)
- **Email:** (can be blank, just press Enter)
- **Password:** (type carefully, won't be visible)
- **Password confirmation:** (type again)

**Example:**
```
Username: admin
Email address: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

---

## 🎨 Static Files Configuration

### Step 1: Understand Static Files

Static files include:
- CSS stylesheets
- JavaScript files
- Images and icons
- Bootstrap files

### Step 2: Collect Static Files

```cmd
python manage.py collectstatic
```

**You'll see:**
```
You have requested to collect static files at the destination
location as specified in your settings:

    C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject\staticfiles

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel:
```

Type `yes` and press Enter.

**Expected output:**
```
Copying 'C:\...\static\css\style.css'
Copying 'C:\...\static\js\main.js'
...
120 static files copied to 'C:\...\staticfiles'.
```

---

## 🚀 Running the Application

### Step 1: Start the Development Server

```cmd
python manage.py runserver
```

**Expected output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 17, 2024 - 14:40:00
Django version 4.2.x, using settings 'tomato_disease.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 2: Access the Application

1. Open your web browser
2. Navigate to: **http://127.0.0.1:8000/**
3. You should see the SmartCrop AI homepage!

### Step 3: Access Admin Panel

1. Navigate to: **http://127.0.0.1:8000/admin/**
2. Login with your superuser credentials
3. You can now manage the application

### Step 4: Stop the Server

Press `CTRL + C` in the Command Prompt to stop the server.

### Step 5: Run on Different Port (Optional)

```cmd
python manage.py runserver 8080
```

Access at: http://127.0.0.1:8080/

### Step 6: Run on Network (Access from Other Devices)

```cmd
python manage.py runserver 0.0.0.0:8000
```

Find your IP address:
```cmd
ipconfig
```

Look for "IPv4 Address" (e.g., `192.168.1.100`)

Access from other devices: `http://192.168.1.100:8000/`

**Important:** Update `ALLOWED_HOSTS` in `settings.py`:
```python
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.100']
```

---

## 🔍 Troubleshooting

### Issue 1: "python is not recognized"

**Solution:**
1. Reinstall Python with "Add to PATH" checked
2. Or manually add to PATH (see Python Installation section)

### Issue 2: "No module named 'django'"

**Solution:**
```cmd
# Make sure virtual environment is activated
venv\Scripts\activate

# Reinstall Django
pip install django
```

### Issue 3: "Error loading model"

**Solution:**
1. Check that model file exists at:
   ```
   C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\models\best_mobilenet_finetuned.keras
   ```
2. Verify path in `settings.py`
3. Ensure TensorFlow is installed:
   ```cmd
   pip install tensorflow
   ```

### Issue 4: "Port already in use"

**Solution:**
```cmd
# Use a different port
python manage.py runserver 8080
```

Or find and kill the process using port 8000:
```cmd
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

### Issue 5: Static files not loading

**Solution:**
```cmd
# Recollect static files
python manage.py collectstatic --noinput

# Clear browser cache (Ctrl + Shift + Delete)
```

### Issue 6: Database locked error

**Solution:**
```cmd
# Close all connections to database
# Delete db.sqlite3 (WARNING: loses all data)
del db.sqlite3

# Recreate database
python manage.py migrate
python manage.py createsuperuser
```

### Issue 7: Permission denied errors

**Solution:**
1. Run Command Prompt as Administrator
2. Or change folder permissions:
   - Right-click project folder
   - Properties → Security → Edit
   - Give your user Full Control

### Issue 8: TensorFlow installation fails

**Solution:**

Install Visual C++ Redistributable:
1. Download from [Microsoft](https://aka.ms/vs/17/release/vc_redist.x64.exe)
2. Install and restart
3. Try installing TensorFlow again:
   ```cmd
   pip install tensorflow-cpu
   ```

---

## 🌐 Production Deployment on Windows

### Option 1: Windows Server with IIS

1. **Install IIS** with CGI support
2. **Install wfastcgi:**
   ```cmd
   pip install wfastcgi
   wfastcgi-enable
   ```
3. **Configure web.config** in project root
4. **Set up IIS site** pointing to project directory

### Option 2: Windows Service with NSSM

1. **Install NSSM** (Non-Sucking Service Manager)
2. **Create batch file** (`run_server.bat`):
   ```batch
   @echo off
   cd C:\path\to\tomatoproject
   venv\Scripts\activate
   python manage.py runserver 0.0.0.0:8000
   ```
3. **Install as service:**
   ```cmd
   nssm install SmartCropAI "C:\path\to\run_server.bat"
   nssm start SmartCropAI
   ```

### Option 3: Waitress (Production WSGI Server)

1. **Install Waitress:**
   ```cmd
   pip install waitress
   ```
2. **Create run script** (`run_production.py`):
   ```python
   from waitress import serve
   from tomato_disease.wsgi import application
   
   serve(application, host='0.0.0.0', port=8000)
   ```
3. **Run:**
   ```cmd
   python run_production.py
   ```

### Production Checklist

- [ ] Set `DEBUG = False` in `settings.py`
- [ ] Configure `SECRET_KEY` (generate new random key)
- [ ] Update `ALLOWED_HOSTS` with your domain/IP
- [ ] Use PostgreSQL instead of SQLite
- [ ] Set up SSL certificate
- [ ] Configure firewall rules
- [ ] Set up automated backups
- [ ] Configure logging
- [ ] Set up monitoring

---

## 📝 Daily Development Workflow

### Starting Work

```cmd
# 1. Navigate to project
cd C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject

# 2. Activate virtual environment
venv\Scripts\activate

# 3. Start development server
python manage.py runserver
```

### Making Changes

```cmd
# If you modify models.py
python manage.py makemigrations
python manage.py migrate

# If you add static files
python manage.py collectstatic

# If you install new packages
pip freeze > requirements.txt
```

### Ending Work

```cmd
# Stop server
CTRL + C

# Deactivate virtual environment
deactivate
```

---

## 🎓 Useful Commands Reference

### Django Management Commands

```cmd
# Create new app
python manage.py startapp app_name

# Open Django shell
python manage.py shell

# Check for problems
python manage.py check

# Show migrations
python manage.py showmigrations

# Create database backup
python manage.py dumpdata > backup.json

# Load database backup
python manage.py loaddata backup.json

# Clear sessions
python manage.py clearsessions

# Run tests
python manage.py test
```

### Virtual Environment Commands

```cmd
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Deactivate
deactivate

# Delete virtual environment
rmdir /s venv
```

### Pip Commands

```cmd
# Install package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Uninstall package
pip uninstall package_name

# List installed packages
pip list

# Show package info
pip show package_name

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Update package
pip install --upgrade package_name

# Update pip itself
python -m pip install --upgrade pip
```

---

## 🆘 Getting Help

### Error Messages

When you encounter an error:
1. Read the **full error message** (scroll up in terminal)
2. Note the **file name** and **line number**
3. Check the **Troubleshooting** section above
4. Search the error on [Stack Overflow](https://stackoverflow.com/)

### Useful Resources

- **Django Documentation:** [docs.djangoproject.com](https://docs.djangoproject.com/)
- **Django Tutorial:** [djangoproject.com/start](https://www.djangoproject.com/start/)
- **TensorFlow Guide:** [tensorflow.org/guide](https://www.tensorflow.org/guide)
- **Python Windows FAQ:** [docs.python.org/3/faq/windows.html](https://docs.python.org/3/faq/windows.html)

### Community Support

- **Django Forum:** [forum.djangoproject.com](https://forum.djangoproject.com/)
- **Stack Overflow:** Tag questions with `django` and `windows`
- **Reddit:** r/django, r/learnpython

---

## ✅ Quick Start Checklist

Use this checklist to ensure everything is set up correctly:

- [ ] Python 3.10 or 3.11 installed
- [ ] Python added to PATH
- [ ] Project downloaded and extracted
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Migrations created (`python manage.py makemigrations`)
- [ ] Migrations applied (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)
- [ ] Static files collected (`python manage.py collectstatic`)
- [ ] Server runs successfully (`python manage.py runserver`)
- [ ] Can access http://127.0.0.1:8000/
- [ ] Can login to admin at http://127.0.0.1:8000/admin/

---

## 🎉 Success!

If you've followed all steps, you should now have:

✅ A fully functional Django development environment on Windows  
✅ The SmartCrop AI application running locally  
✅ Admin access to manage the application  
✅ Understanding of how to start/stop the server  
✅ Knowledge of common troubleshooting steps  

**Next Steps:**
- Explore the application features
- Upload tomato leaf images for disease detection
- Check the admin panel
- Customize the application to your needs
- Deploy to production when ready

---

## 📞 Support

For additional help:
- Check the main [README.md](README.md) for project overview
- Review Django's [Windows installation guide](https://docs.djangoproject.com/en/stable/howto/windows/)
- Contact the development team

---

**SmartCrop AI** - AI-Powered Tomato Disease Detection  
Built with ❤️ for Windows Users | Empowering Smart Agriculture

*Last Updated: December 2024*
