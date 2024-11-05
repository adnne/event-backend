PROJECT SETUP GUIDE

INITIAL SETUP
- Clone the repository to your local machine
git clone <repository-url>

- Navigate to the project directory
cd <project-folder>

ENVIRONMENT SETUP
- Create a virtual environment to isolate project dependencies
python -m venv env

- Activate the virtual environment (Windows)
env\Scripts\activate

- Activate the virtual environment (Linux/Mac)
# source env/bin/activate

DEPENDENCIES INSTALLATION
- Install all required packages
pip install -r requirements.txt

DATABASE SETUP
- Apply database migrations
python manage.py migrate

ADMIN ACCOUNT SETUP
- Create an administrator account (will prompt for username, email, password)
python manage.py createsuperuser

RUNNING THE SERVER
- Start server with your IP address for network access
python manage.py runserver <your-ip-address>

- For local development only
python manage.py runserver
