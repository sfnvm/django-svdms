# Setup Virtual Environment
## First step: Clone source
$ cd django-svdms  
$ virtualenv env  
$ source env/bin/activate  

# Create default Superuser
$ python manage.py createsuperuser --email trungpt.dev@gmail.com --username trungpt  
// my password: 0812

# Tech-Stack
Django  
DRF  
Postgres
Postgis // for geometric and location tracking usage  
