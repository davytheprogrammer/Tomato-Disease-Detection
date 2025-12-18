# 📚 Windows Documentation Index

Complete guide to running SmartCrop AI (Tomato Disease Detection) on Windows.

---

## 🎯 Choose Your Path

### 🚀 I want to get started quickly!
**→ [WINDOWS_QUICKSTART.md](WINDOWS_QUICKSTART.md)**
- 5-minute setup
- Just the commands
- Automated batch files
- Perfect for: Testing, development, learning

### 📖 I want detailed instructions
**→ [WINDOWS_SETUP.md](WINDOWS_SETUP.md)**
- Complete step-by-step guide
- Explanations for each step
- Troubleshooting section
- Perfect for: First-time users, understanding the process

### 🏢 I want to deploy to production
**→ [WINDOWS_PRODUCTION.md](WINDOWS_PRODUCTION.md)**
- Windows Server deployment
- IIS and Waitress setup
- Security hardening
- Monitoring and backups
- Perfect for: Production environments, Windows Server

---

## 📁 What's Included

### Documentation Files

| File | Purpose | Audience |
|------|---------|----------|
| **WINDOWS_QUICKSTART.md** | Fast setup with minimal explanation | Developers who want to start quickly |
| **WINDOWS_SETUP.md** | Detailed setup with troubleshooting | First-time users, learners |
| **WINDOWS_PRODUCTION.md** | Production deployment guide | System administrators, DevOps |
| **README.md** | Project overview and general setup | All users |

### Automated Tools (in `tomatoproject/` folder)

| File | Purpose | When to Use |
|------|---------|-------------|
| **SETUP.bat** | Automated initial setup | First time setup |
| **START_SERVER.bat** | Start Django development server | Every time you want to run the app |
| **TROUBLESHOOT.bat** | Interactive troubleshooting menu | When you encounter problems |

---

## 🎓 Learning Path

### Beginner Path
1. Read [WINDOWS_QUICKSTART.md](WINDOWS_QUICKSTART.md)
2. Run `SETUP.bat` in the `tomatoproject` folder
3. Run `START_SERVER.bat` to start the application
4. Access http://127.0.0.1:8000/
5. If issues arise, run `TROUBLESHOOT.bat`

### Intermediate Path
1. Read [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
2. Follow manual setup commands
3. Understand each step
4. Customize as needed
5. Refer to troubleshooting section when needed

### Advanced Path
1. Complete beginner or intermediate setup
2. Read [WINDOWS_PRODUCTION.md](WINDOWS_PRODUCTION.md)
3. Set up Windows Server environment
4. Configure PostgreSQL database
5. Deploy with IIS or Waitress
6. Set up monitoring and backups

---

## 🔧 Quick Reference

### Common Commands

```cmd
# Navigate to project
cd C:\Users\YourUsername\Documents\Tomato_Disease_Detection-main\tomatoproject

# Activate virtual environment
venv\Scripts\activate

# Start development server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

### Automated Tools

```cmd
# First time setup
SETUP.bat

# Start server
START_SERVER.bat

# Troubleshoot issues
TROUBLESHOOT.bat
```

### Important URLs

- **Main Application:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Upload Page:** http://127.0.0.1:8000/upload/
- **Disease Info:** http://127.0.0.1:8000/disease-info/

---

## 🆘 Getting Help

### Step 1: Check Documentation
1. Review the appropriate guide for your use case
2. Check the troubleshooting section
3. Run `TROUBLESHOOT.bat` for automated diagnostics

### Step 2: Common Issues

| Issue | Solution | Reference |
|-------|----------|-----------|
| "python is not recognized" | Reinstall Python with PATH option | [WINDOWS_SETUP.md](WINDOWS_SETUP.md#python-installation) |
| "No module named django" | Activate venv and reinstall | [WINDOWS_SETUP.md](WINDOWS_SETUP.md#troubleshooting) |
| Port already in use | Use different port or kill process | [WINDOWS_SETUP.md](WINDOWS_SETUP.md#troubleshooting) |
| Model not loading | Check model path in settings | [WINDOWS_SETUP.md](WINDOWS_SETUP.md#troubleshooting) |
| Static files not loading | Run collectstatic | [WINDOWS_SETUP.md](WINDOWS_SETUP.md#static-files-configuration) |

### Step 3: External Resources
- **Django Documentation:** https://docs.djangoproject.com/
- **Python Windows FAQ:** https://docs.python.org/3/faq/windows.html
- **Stack Overflow:** Tag questions with `django` and `windows`

---

## ✅ Setup Checklist

Use this to track your progress:

### Development Setup
- [ ] Python 3.10+ installed
- [ ] Python added to PATH
- [ ] Project downloaded
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Migrations applied
- [ ] Superuser created
- [ ] Static files collected
- [ ] Server runs successfully
- [ ] Can access application in browser

### Production Setup (Additional)
- [ ] Windows Server prepared
- [ ] PostgreSQL installed
- [ ] Production dependencies installed
- [ ] Environment variables configured
- [ ] SSL certificate installed
- [ ] Firewall configured
- [ ] Windows Service created
- [ ] Backups scheduled
- [ ] Monitoring configured
- [ ] Security hardened

---

## 📊 Documentation Structure

```
Tomato_Disease_Detection-main/
├── README.md                    # Main project overview
├── WINDOWS_QUICKSTART.md        # Quick start guide
├── WINDOWS_SETUP.md             # Detailed setup guide
├── WINDOWS_PRODUCTION.md        # Production deployment
└── tomatoproject/
    ├── README.md                # Django project README
    ├── SETUP.bat                # Automated setup
    ├── START_SERVER.bat         # Server launcher
    └── TROUBLESHOOT.bat         # Troubleshooting tool
```

---

## 🎯 Next Steps

### After Setup
1. **Explore the application**
   - Upload tomato leaf images
   - Test disease detection
   - Check admin panel

2. **Customize**
   - Update branding
   - Modify disease information
   - Adjust UI/UX

3. **Deploy**
   - Follow production guide
   - Set up monitoring
   - Configure backups

### Learning Resources
- **Django Tutorial:** https://docs.djangoproject.com/en/stable/intro/tutorial01/
- **TensorFlow Guide:** https://www.tensorflow.org/tutorials
- **Python Documentation:** https://docs.python.org/3/

---

## 📞 Support

### Documentation Issues
If you find errors or have suggestions for improving this documentation:
1. Check if the issue is already addressed
2. Review all relevant guides
3. Contact the development team

### Application Issues
For bugs or feature requests:
1. Use `TROUBLESHOOT.bat` for diagnostics
2. Check error logs in `logs/` folder
3. Review troubleshooting sections
4. Contact support with error details

---

## 🔄 Updates

This documentation is regularly updated. Check for:
- New features
- Security updates
- Bug fixes
- Performance improvements

**Last Updated:** December 2024  
**Documentation Version:** 1.0  
**Supported Windows Versions:** Windows 10, Windows 11, Windows Server 2016+

---

## 🎉 Success!

You now have access to comprehensive Windows documentation for SmartCrop AI!

**Choose your path:**
- 🚀 Quick Start → [WINDOWS_QUICKSTART.md](WINDOWS_QUICKSTART.md)
- 📖 Detailed Guide → [WINDOWS_SETUP.md](WINDOWS_SETUP.md)
- 🏢 Production → [WINDOWS_PRODUCTION.md](WINDOWS_PRODUCTION.md)

**Happy coding!** 🌱🍅

---

**SmartCrop AI** - AI-Powered Tomato Disease Detection  
Built with ❤️ for Windows Users | Empowering Smart Agriculture
