# Setup Virtual Environment
## First step:  
* Clone this shit to your computer  
* I assume that you already installed:
    - PostgreSQL v12
    - PostgreSQL Extension: PostGIS

## ... Then execute commands below
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
- 'rest_framework',  
- 'django.contrib.gis',  
- 'channels'

DRF  
PostgreSQL  
PostGIS  
Redis  