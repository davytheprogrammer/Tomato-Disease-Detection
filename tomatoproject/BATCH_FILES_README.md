# 🔧 Windows Batch File Utilities

**Automated tools to make Django development on Windows easier!**

---

## 📁 Files Overview

This folder contains three powerful batch files that automate common Django tasks on Windows:

| File | Purpose | When to Use |
|------|---------|-------------|
| **SETUP.bat** | Complete initial setup | First time only |
| **START_SERVER.bat** | Start Django server | Every time you work |
| **TROUBLESHOOT.bat** | Fix common issues | When problems occur |

---

## 🚀 SETUP.bat - Initial Setup

### What It Does
Automatically performs the complete Django setup:
1. ✅ Creates virtual environment
2. ✅ Installs all dependencies
3. ✅ Runs database migrations
4. ✅ Collects static files
5. ✅ Creates admin user

### How to Use
1. Navigate to the `tomatoproject` folder
2. Double-click **SETUP.bat**
3. Wait for dependencies to install (5-10 minutes)
4. Enter admin credentials when prompted
5. Done! You're ready to start the server

### What You'll See
```
========================================
  SmartCrop AI - Initial Setup
========================================

This script will:
  1. Create virtual environment
  2. Install dependencies
  3. Run database migrations
  4. Collect static files
  5. Create admin user

This may take 5-10 minutes...

Press any key to continue . . .
```

### When to Use
- ✅ First time setting up the project
- ✅ After deleting the virtual environment
- ✅ When starting fresh

### When NOT to Use
- ❌ If you've already run setup
- ❌ Just to start the server (use START_SERVER.bat)
- ❌ To fix issues (use TROUBLESHOOT.bat)

---

## ▶️ START_SERVER.bat - Server Launcher

### What It Does
Starts the Django development server:
1. ✅ Activates virtual environment
2. ✅ Checks if setup is complete
3. ✅ Starts Django server
4. ✅ Shows access URLs

### How to Use
1. Navigate to the `tomatoproject` folder
2. Double-click **START_SERVER.bat**
3. Wait for server to start
4. Open browser to http://127.0.0.1:8000/
5. Press CTRL+C to stop when done

### What You'll See
```
========================================
  SmartCrop AI - Starting Server
========================================

[1/3] Activating virtual environment...
[2/3] Starting Django development server...

========================================
  Server will start at:
  http://127.0.0.1:8000/

  Admin panel:
  http://127.0.0.1:8000/admin/

  Press CTRL+C to stop the server
========================================
```

### When to Use
- ✅ Every time you want to run the application
- ✅ For development and testing
- ✅ To show the app to others

### Error Messages

**"Virtual environment not found!"**
- Solution: Run SETUP.bat first

**"Django is not installed!"**
- Solution: Run SETUP.bat or manually install dependencies

**"Database not found"**
- The script will automatically run migrations

---

## 🔍 TROUBLESHOOT.bat - Interactive Troubleshooting

### What It Does
Provides an interactive menu to diagnose and fix issues:
1. ✅ Check Python installation
2. ✅ Verify virtual environment
3. ✅ Check Django installation
4. ✅ Check database
5. ✅ Reset database (with warning)
6. ✅ Reinstall dependencies
7. ✅ Check port availability
8. ✅ View system information

### How to Use
1. Navigate to the `tomatoproject` folder
2. Double-click **TROUBLESHOOT.bat**
3. Select option from menu (1-9)
4. Follow on-screen instructions
5. Select option 9 to exit

### Menu Options

#### 1. Check Python Installation
- Verifies Python is installed
- Checks Python version
- Verifies pip is available

**Use when:** "python is not recognized" error

#### 2. Check Virtual Environment
- Verifies venv folder exists
- Shows Python path
- Lists installed packages

**Use when:** Virtual environment issues

#### 3. Check Django Installation
- Verifies Django is installed
- Shows Django version

**Use when:** "No module named 'django'" error

#### 4. Check Database
- Verifies database file exists
- Shows database size
- Lists migrations

**Use when:** Database errors

#### 5. Reset Database
- **WARNING:** Deletes all data!
- Removes database file
- Runs fresh migrations
- Creates new superuser

**Use when:** Database is corrupted or you want to start fresh

#### 6. Reinstall Dependencies
- Upgrades pip
- Reinstalls all packages
- Updates to latest versions

**Use when:** Package errors or missing modules

#### 7. Check Port Availability
- Shows if port 8000 is in use
- Displays process using the port
- Suggests solutions

**Use when:** "Port already in use" error

#### 8. View System Information
- Windows version
- Python version
- pip version
- Current directory
- Virtual environment status
- Database status
- Available memory

**Use when:** Need to diagnose system issues

---

## 📋 Common Workflows

### First Time Setup
```
1. Double-click SETUP.bat
2. Wait for completion
3. Double-click START_SERVER.bat
4. Access http://127.0.0.1:8000/
```

### Daily Development
```
1. Double-click START_SERVER.bat
2. Develop and test
3. Press CTRL+C when done
```

### When Problems Occur
```
1. Double-click TROUBLESHOOT.bat
2. Select appropriate option
3. Follow instructions
4. Try START_SERVER.bat again
```

### Starting Fresh
```
1. Double-click TROUBLESHOOT.bat
2. Select option 5 (Reset Database)
3. Confirm with "YES"
4. Create new superuser
5. Double-click START_SERVER.bat
```

---

## 🆘 Troubleshooting the Troubleshooter

### Batch File Won't Run

**Error: "Windows protected your PC"**
- Click "More info"
- Click "Run anyway"

**Error: "This app can't run on your PC"**
- Right-click the file
- Select "Properties"
- Click "Unblock"
- Click "OK"
- Try again

### Batch File Closes Immediately

**Solution:**
- Right-click the batch file
- Select "Edit"
- Check for errors
- Or run from Command Prompt to see errors:
  ```cmd
  cd C:\path\to\tomatoproject
  SETUP.bat
  ```

---

## 🔧 Advanced Usage

### Running from Command Prompt

For more control, run batch files from Command Prompt:

```cmd
# Navigate to project
cd C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject

# Run setup
SETUP.bat

# Run server
START_SERVER.bat

# Run troubleshooter
TROUBLESHOOT.bat
```

### Modifying Batch Files

You can customize these batch files:

1. Right-click the file
2. Select "Edit"
3. Make changes
4. Save
5. Test

**Common modifications:**
- Change server port
- Add custom commands
- Modify paths
- Add logging

---

## 📊 What Each File Checks

### SETUP.bat Checks
- ✅ Python installation
- ✅ Virtual environment creation
- ✅ Dependency installation
- ✅ Database migrations
- ✅ Static files collection

### START_SERVER.bat Checks
- ✅ Virtual environment exists
- ✅ Django is installed
- ✅ Database exists (creates if missing)
- ✅ Server starts successfully

### TROUBLESHOOT.bat Checks
- ✅ Python and pip installation
- ✅ Virtual environment status
- ✅ Django installation
- ✅ Database integrity
- ✅ Port availability
- ✅ System resources

---

## 💡 Tips and Best Practices

### DO:
- ✅ Run SETUP.bat only once
- ✅ Use START_SERVER.bat daily
- ✅ Use TROUBLESHOOT.bat when issues occur
- ✅ Keep batch files in the project folder
- ✅ Read error messages carefully

### DON'T:
- ❌ Run SETUP.bat repeatedly
- ❌ Delete batch files
- ❌ Modify without understanding
- ❌ Run as administrator unless needed
- ❌ Ignore error messages

---

## 🎯 Quick Reference

| Task | Command |
|------|---------|
| First setup | Double-click `SETUP.bat` |
| Start server | Double-click `START_SERVER.bat` |
| Stop server | Press `CTRL+C` |
| Fix issues | Double-click `TROUBLESHOOT.bat` |
| Reset database | `TROUBLESHOOT.bat` → Option 5 |
| Check Python | `TROUBLESHOOT.bat` → Option 1 |
| Reinstall packages | `TROUBLESHOOT.bat` → Option 6 |

---

## 📞 Getting Help

If batch files don't solve your issue:

1. **Check Documentation:**
   - [WINDOWS_QUICKSTART.md](../WINDOWS_QUICKSTART.md)
   - [WINDOWS_SETUP.md](../WINDOWS_SETUP.md)

2. **Run Manual Commands:**
   - See detailed guides for step-by-step instructions

3. **Check Logs:**
   - Look in `logs/` folder for error details

4. **Contact Support:**
   - Provide error messages
   - Mention which batch file you used
   - Include system information from TROUBLESHOOT.bat option 8

---

## 🎉 Success!

These batch files make Django development on Windows:
- ⚡ **Faster** - Automated setup
- 🎯 **Easier** - One-click operations
- 🔧 **Safer** - Built-in error checking
- 📚 **Beginner-friendly** - No command line needed

**Happy developing!** 🚀

---

**SmartCrop AI** - Windows Batch Utilities  
*Making Django development on Windows a breeze* 🪟✨
