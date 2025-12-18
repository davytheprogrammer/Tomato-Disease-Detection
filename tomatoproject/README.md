# SmartCrop AI - Django Web Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2%2B-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13%2B-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

A professional Django web application for tomato disease detection using deep learning. Built with a modern Bootstrap 5 interface, this AI-powered system enables farmers to identify tomato leaf diseases instantly and receive treatment recommendations.

## 🎯 Features

### Core Functionality
- **Single Image Upload** - Upload and analyze individual tomato leaf images
- **Batch Processing** - Analyze multiple images simultaneously for field surveys
- **Real-time Predictions** - Get AI-powered disease detection results in seconds
- **Treatment Recommendations** - Receive actionable treatment advice for each disease

### Professional Interface
- **Modern UI** - Built with Bootstrap 5 and custom CSS
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile devices
- **Analytics Dashboard** - Track prediction history and disease trends
- **Disease Library** - Comprehensive database of tomato diseases with detailed information

### AI Performance
- **95% Accuracy** - Fine-tuned MobileNetV2 model on 10,000+ images
- **10 Disease Classes** - Detects all major tomato leaf diseases
- **Fast Inference** - Optimized for real-time predictions
- **Confidence Scores** - Shows model confidence for each prediction

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip package manager
- 2GB+ available RAM
- Modern web browser

### Installation

1. **Clone the repository** (or use your existing project):
```bash
git clone <repository-url>
cd tomatoproject
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Copy your model file**:
Place your trained model at:
```
/home/ogega/Projects/Tomato_Disease_Detection-main/models/best_mobilenet_finetuned.keras
```

6. **Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create superuser** (optional):
```bash
python manage.py createsuperuser
```

8. **Collect static files**:
```bash
python manage.py collectstatic
```

9. **Run development server**:
```bash
python manage.py runserver
```

10. **Access the application**:
Open your browser and go to: `http://127.0.0.1:8000`

## 🪟 Windows Users - Automated Tools

**Windows users can use these batch files for easier setup:**

### First Time Setup
Double-click **`SETUP.bat`** to automatically:
- Create virtual environment
- Install all dependencies
- Run database migrations
- Collect static files
- Create admin user

### Start the Server
Double-click **`START_SERVER.bat`** to:
- Activate virtual environment
- Start Django development server
- Open at http://127.0.0.1:8000/

### Troubleshooting
Double-click **`TROUBLESHOOT.bat`** for an interactive menu to:
- Check Python installation
- Verify virtual environment
- Check Django installation
- Reset database
- Reinstall dependencies
- Check port availability
- View system information

**For detailed Windows instructions, see:**
- Quick Start: [WINDOWS_QUICKSTART.md](../WINDOWS_QUICKSTART.md)
- Complete Guide: [WINDOWS_SETUP.md](../WINDOWS_SETUP.md)

---

## 📁 Project Structure

```
tomatoproject/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment config
├── runtime.txt                  # Python version for Heroku
├── .env.example                 # Environment variables template
├── tomato_disease/              # Main Django project
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL configuration
│   ├── wsgi.py                 # WSGI application entry
│   └── asgi.py                 # ASGI application entry
├── tomato_app/                  # Main Django app
│   ├── migrations/             # Database migrations
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── forms.py                # Django forms
│   ├── urls.py                 # App URL patterns
│   ├── admin.py                # Django admin configuration
│   ├── apps.py                 # App configuration
│   ├── ml_model.py             # ML model wrapper class
│   ├── disease_info.py         # Disease database
│   └── __init__.py
├── templates/
│   └── tomato_app/             # HTML templates
│       ├── base.html           # Base template
│       ├── index.html          # Landing page
│       ├── upload_image.html   # Single image upload
│       ├── batch_predict.html  # Batch upload
│       ├── prediction_result.html
│       ├── disease_info.html   # Disease library
│       ├── crop_report.html    # Analytics dashboard
│       ├── model_performance.html
│       └── about.html
├── static/                      # Static files
│   ├── css/
│   │   └── style.css           # Custom styles
│   ├── js/
│   │   └── main.js             # JavaScript files
│   └── images/                 # Images and icons
└── media/                       # User uploads
    ├── uploads/
    └── predictions/
```

## 🌐 Pages Overview

### 1. Home Page (`/`)
- Professional landing page with hero section
- Feature highlights
- Statistics and metrics
- Quick access to upload functionality

### 2. Image Upload (`/upload/`)
- Drag-and-drop image upload
- Single image processing
- Real-time prediction results
- Confidence score visualization

### 3. Batch Predict (`/batch-predict/`)
- Multiple image upload
- Batch processing interface
- Support for up to 10 images
- Process all images with one click

### 4. Disease Info (`/disease-info/`)
- Comprehensive disease library
- Browse all 10 disease classes
- Scientific names and symptoms
- Treatment recommendations
- Printable disease fact sheets

### 5. Crop Report (`/crop-report/`)
- Analytics dashboard
- Prediction history
- Disease distribution charts
- Download CSV reports
- Track farm health trends

### 6. Model Performance (`/model-performance/`)
- Technical performance metrics
- Accuracy: 95%
- Per-class evaluation
- Confusion matrix explanation
- Model architecture details

### 7. About (`/about/`)
- Project mission and vision
- Technology overview
- Development team
- Contact information

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
# Security
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=False

# Allowed Hosts (comma-separated)
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com,www.your-domain.com

# Database (optional - PostgreSQL)
DATABASE_URL=postgres://username:password@localhost:5432/tomato_ai

# Custom Model Path (optional)
MODEL_PATH=/path/to/your/model.keras
```

### Django Settings

Key settings in `tomato_disease/settings.py`:

- `MODEL_PATH` - Path to your trained model
- `STATIC_ROOT` - Static files collection point
- `MEDIA_ROOT` - User upload storage
- `STATICFILES_STORAGE` - Whitenoise for production

### Model Configuration

The application expects a TensorFlow Keras model saved as `.keras` format.

**Model Requirements:**
- Input shape: `(224, 224, 3)`
- Output classes: 10
- Output format: Probability distribution
- Preprocessing: Image resize to 224x224, normalize to [0,1]

**Default Model Location:**
- Development: `../models/best_mobilenet_finetuned.keras`
- Production: Place in `models/` directory

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Configure `SECRET_KEY` (random 50+ character string)
- [ ] Set `ALLOWED_HOSTS` with your domain
- [ ] Configure database (PostgreSQL recommended)
- [ ] Set up static file serving (Whitenoise configured)
- [ ] Configure HTTPS/SSL
- [ ] Set up media file storage (S3 recommended)
- [ ] Configure logging
- [ ] Set up error monitoring
- [ ] Backup strategy

### Heroku Deployment

1. **Install Heroku CLI** and login

2. **Create Heroku app**:
```bash
heroku create your-app-name
```

3. **Add buildpacks**:
```bash
heroku buildpacks:add heroku/python
```

4. **Configure environment variables**:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
```

5. **Enable PostgreSQL** (optional):
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

6. **Deploy**:
```bash
git push heroku main
```

7. **Run migrations**:
```bash
heroku run python manage.py migrate
```

8. **Create superuser**:
```bash
heroku run python manage.py createsuperuser
```

9. **Access logs**:
```bash
heroku logs --tail
```

### Docker Deployment

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "tomato_disease.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t smartcrop-ai .
docker run -p 8000:8000 smartcrop-ai
```

### DigitalOcean / VPS Deployment

1. **Clone repository** on server
2. **Install Python and dependencies**
3. **Install and configure PostgreSQL** (optional)
4. **Set up Gunicorn** with systemd service
5. **Configure Nginx** as reverse proxy
6. **Enable SSL with Let's Encrypt**
7. **Set up supervisor** for process management

## 🔒 Security Considerations

- Always use HTTPS in production
- Set strong `SECRET_KEY` (50+ random characters)
- Never commit `.env` file to version control
- Use environment variables for sensitive data
- Limit upload file sizes (configured in settings)
- Validate file types before processing
- Use Django's built-in CSRF protection
- Configure proper CORS headers if using API

## 📊 Database

### Default: SQLite
Perfect for development and small-scale deployments.

### Production: PostgreSQL
Recommended for production environments.

**Setup:**
```bash
# Install PostgreSQL
sudo apt-get install postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql
createdb tomato_ai
CREATE USER tomato_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE tomato_ai TO tomato_user;
```

Configure in `.env`:
```
DATABASE_URL=postgres://tomato_user:your_password@localhost:5432/tomato_ai
```

## 🎨 Customization

### Branding
- Update logo/favicon in `static/images/`
- Modify colors in `static/css/style.css`
- Change app name in `templates/tomato_app/base.html`

### Disease Information
Update `tomato_app/disease_info.py` to modify:
- Disease names and descriptions
- Treatment recommendations
- Scientific information

### Templates
All templates are in `templates/tomato_app/`:
- Use Bootstrap 5 components
- Maintain responsive design
- Follow Django template conventions

## 📈 Monitoring

### Django Admin
Access admin panel at `/admin/` to:
- View prediction logs
- Manage users (if authentication added)
- Monitor system activity

### Logging
Configure logging in `settings.py`:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

## 📱 API Usage

The application includes a REST API endpoint:

**Endpoint**: `POST /api/predict/`

**Request**:
```bash
curl -X POST -F "image=@tomato_leaf.jpg" http://localhost:8000/api/predict/
```

**Response**:
```json
{
  "success": true,
  "prediction": {
    "class": "Early Blight",
    "confidence": 0.87
  },
  "all_predictions": [...]
}
```

## 🐛 Troubleshooting

**Model not loading:**
- Check MODEL_PATH in settings
- Verify model file exists
- Check TensorFlow installation

**Static files not loading:**
- Run `python manage.py collectstatic`
- Check STATIC_ROOT permissions
- Verify Whitenoise middleware

**Upload issues:**
- Check MEDIA_ROOT permissions
- Verify file size limits
- Validate image format

**Database errors:**
- Run migrations: `python manage.py migrate`
- Check database connection
- Verify DATABASE_URL

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Heroku Dev Center](https://devcenter.heroku.com/)

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact the development team
- Check troubleshooting section

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**SmartCrop AI** - AI-Powered Tomato Disease Detection
Built with ❤️ by Data Safari Team | Empowering Smart Agriculture
