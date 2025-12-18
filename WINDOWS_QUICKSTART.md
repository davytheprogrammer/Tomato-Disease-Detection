# 🚀 Windows Quick Start - 5 Minutes to Running

**Just want to get started fast?** Choose your method:

## 🎯 Option 1: Automated Setup (Easiest!)

1. Navigate to the `tomatoproject` folder
2. Double-click **`SETUP.bat`** to run initial setup
3. Follow the prompts to create admin user
4. Double-click **`START_SERVER.bat`** to start the server
5. Open browser to http://127.0.0.1:8000/

**That's it!** The batch files handle everything automatically.

---

## ⌨️ Option 2: Manual Setup (More Control)

**Just want to get started fast?** Follow these commands in order.

## Prerequisites
- Windows 10/11
- Python 3.10 or 3.11 installed ([Download here](https://www.python.org/downloads/))
- Python added to PATH during installation

## Step-by-Step Commands

### 1. Open Command Prompt
Press `Win + R`, type `cmd`, press Enter

### 2. Navigate to Project
```cmd
cd C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject
```
*(Replace `YourUsername` with your actual Windows username)*

### 3. Create Virtual Environment
```cmd
python -m venv venv
```

### 4. Activate Virtual Environment
```cmd
venv\Scripts\activate
```
You should see `(venv)` at the start of your command line.

### 5. Install Dependencies
```cmd
pip install -r requirements.txt
```
⏱️ *This takes 5-10 minutes*

### 6. Run Migrations
```cmd
python manage.py migrate
```

### 7. Create Admin User
```cmd
python manage.py createsuperuser
```
Enter username, email (optional), and password when prompted.

### 8. Collect Static Files
```cmd
python manage.py collectstatic
```
Type `yes` when asked.

### 9. Start Server
```cmd
python manage.py runserver
```

### 10. Open Browser
Navigate to: **http://127.0.0.1:8000/**

## ✅ You're Done!

- **Main App:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Stop Server
Press `CTRL + C` in Command Prompt

## Next Time You Start

```cmd
cd C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject
venv\Scripts\activate
python manage.py runserver
```

## Having Issues?

See the full guide: **[WINDOWS_SETUP.md](WINDOWS_SETUP.md)**

## Common Errors

**"python is not recognized"**
- Reinstall Python with "Add to PATH" checked

**"No module named 'django'"**
- Make sure virtual environment is activated: `venv\Scripts\activate`
- Reinstall: `pip install django`

**"Execution policy" error**
- Open PowerShell as Admin
- Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Port already in use**
- Use different port: `python manage.py runserver 8080`

---

**Need more help?** Check [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for detailed explanations and troubleshooting.
