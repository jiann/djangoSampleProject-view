# djangoSampleProject
django Project from Coursera IBM

#Setup environment
python3 -m pip install -U -r requirements.txt

#Migrate model
python3 manage.py makemigrations
python3 manage.py migrate

#Develop
python3 manage.py runserver

#How to build
create model (in models.py)
configure the route (in urls.py)
