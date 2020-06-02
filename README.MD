# Setup Virtual Environment
## First step: Clone this source
$ cd django-svdms  
$ virtualenv env  
$ source env/bin/activate  
$ pip install -r requirement.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

# Create default Superuser
$ python manage.py createsuperuser --email trungpt.dev@gmail.com --username trungpt  
// my password: 0812

# Tech-stack
Django  
DRF  
Postgres  
Postgis  
Redis  