##### Project Setup Guide

###### Initial Setup
# Clone the repository to your local machine
git clone <repository-url>

# Navigate to the project directory
cd <project-folder>

###### Environment Setup
# Create a virtual environment to isolate project dependencies
python -m venv env

# Activate the virtual environment
# Note: On Windows, use this command
env\Scripts\activate
# Note: On Linux/Mac, use this command instead
# source env/bin/activate

###### Dependencies Installation
# Install all required packages defined in requirements.txt
pip install -r requirements.txt

###### Database Setup
# Apply database migrations to set up your database schema
python manage.py migrate

###### Admin Account Setup
# Create an administrator account to access the Django admin interface
# You'll be prompted to enter username, email, and password
python manage.py createsuperuser

###### Running the Server
# Start the development server with your IP address
# Replace <your-ip-address> with your actual IP (e.g., 192.168.1.100:8000)
# This allows other devices on your network to access the application
python manage.py runserver <your-ip-address>

# For local development only, you can use:
# python manage.py runserver
