Project Setup Guide
------------------

Initial Setup
------------
# Clone the repository to your local machine
git clone <repository-url>

# Navigate to the project directory
cd <project-folder>

Environment Setup
---------------
# Create a virtual environment to isolate project dependencies
python -m venv env

# Activate the virtual environment (Windows)
env\Scripts\activate

# Activate the virtual environment (Linux/Mac)
# source env/bin/activate

Dependencies Installation
-----------------------
# Install all required packages
pip install -r requirements.txt

Database Setup
-------------
# Apply database migrations
python manage.py migrate

Admin Account Setup
-----------------
# Create an administrator account
# You'll be prompted for username, email, and password
python manage.py createsuperuser

Running the Server
----------------
# Start server with your IP address for network access
# Example: python manage.py runserver 192.168.1.100:8000
python manage.py runserver <your-ip-address>

# For local development only
python manage.py runserver
