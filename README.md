
git clone <repository-url>
cd <project-folder>

#create env variables 
python -m venv env
env\Scripts\activate

#install requirements
pip install -r requirements.txt

#run migrations
python manage.py migrate

#create user to access the admin 
python manage.py createsuperuser

#add your ip address so later you connect it with the app 
python manage.py runserver <your-ip-address>
