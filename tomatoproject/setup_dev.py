#!/usr/bin/env python
"""
Setup script for SmartCrop AI Django Application
Automates the initial setup process
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description=""):
    """Run a shell command and handle errors"""
    print(f"📦 {description or command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return False
    print("✅ Done")
    return True


def check_and_install_requirements():
    """Check if requirements are installed and install if needed"""
    print("🔍 Checking requirements...")
    try:
        import django, tensorflow, PIL, numpy, pandas
        print("✅ All requirements already installed")
        return True
    except ImportError as e:
        print(f"📥 Installing missing packages: {e}")
        return run_command("pip install -r requirements.txt", "Installing requirements")


def setup_database():
    """Set up the database with migrations"""
    print("🗄️  Setting up database...")
    steps = [
        ("python manage.py makemigrations", "Creating migrations"),
        ("python manage.py migrate", "Applying migrations"),
    ]
    for command, desc in steps:
        if not run_command(command, desc):
            return False
    return True


def create_env_file():
    """Create .env file if it doesn't exist"""
    env_path = Path(".env")
    if not env_path.exists():
        print("📝 Creating .env file...")
        env_example = Path(".env.example")
        if env_example.exists():
            import shutil
            shutil.copy(env_example, env_path)
            print("✅ .env file created from .env.example")
            print("⚠️  Please edit .env with your settings")
        else:
            # Create default .env
            default_env = """SECRET_KEY=django-insecure-dev-key-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
"""
            env_path.write_text(default_env)
            print("✅ .env file created with default settings")
    else:
        print("✅ .env file already exists")


def check_model_file():
    """Check if model file exists"""
    print("🤖 Checking for model file...")

    # Check common locations
    model_locations = [
        Path("../models/best_mobilenet_finetuned.keras"),
        Path("models/best_mobilenet_finetuned.keras"),
        Path("best_mobilenet_finetuned.keras"),
    ]

    for location in model_locations:
        if location.exists():
            print(f"✅ Model found at: {location}")
            return True

    print("❌ Model file not found!")
    print("\nPlease ensure your trained model is available at one of these locations:")
    for loc in model_locations:
        print(f"  - {loc}")
    print("\nExpected: best_mobilenet_finetuned.keras")
    return False


def run_tests():
    """Run basic tests"""
    print("🧪 Running basic tests...")
    try:
        # Test Django setup
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tomato_disease.settings')
        import django
        django.setup()

        # Test model loading
        from tomato_app.ml_model import predictor
        if predictor._model is None:
            print("⚠️  Model not loaded (expected if model file is missing)")
        else:
            print("✅ Model loaded successfully")

        # Test database connection
        from django.db import connection
        connection.ensure_connection()
        print("✅ Database connection successful")

        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def collect_static():
    """Collect static files"""
    print("📂 Collecting static files...")
    return run_command("python manage.py collectstatic --noinput", "Collecting static files")


def main():
    """Main setup function"""
    print("🍅 SmartCrop AI - Setup Script")
    print("=" * 50)

    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)

    steps = [
        (check_and_install_requirements, "Checking requirements"),
        (create_env_file, "Creating environment file"),
        (setup_database, "Setting up database"),
        (check_model_file, "Checking model file"),
        (collect_static, "Collecting static files"),
        (run_tests, "Running tests"),
    ]

    all_passed = True
    for step_func, description in steps:
        print(f"\n{description}...")
        print("-" * 30)
        if not step_func():
            all_passed = False
            response = input("Continue anyway? (y/n): ")
            if response.lower() != 'y':
                sys.exit(1)

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 Setup completed successfully!")
        print("\nTo start the development server:")
        print("  python manage.py runserver")
        print("\nThen open: http://127.0.0.1:8000")
        print("\nTo create a superuser (for admin access):")
        print("  python manage.py createsuperuser")
    else:
        print("⚠️  Setup completed with warnings")
        print("\nPlease address the issues above before running the server")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)
