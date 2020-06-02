# Setup Virtual Environment
## First step: Clone this source
$ cd django-svdms  
$ virtualenv env  
$ source env/bin/activate  
$ pip install -r requirement.txt

# Create default Superuser
$ python manage.py createsuperuser --email trungpt.dev@gmail.com --username trungpt  
// my password: 0812

# Tech-Stack
Django  
DRF  
Postgres
Postgis
