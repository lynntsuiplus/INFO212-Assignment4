Group 1 Oblig Group 2  
* Jakob Andreassen  
* Leander Giskegjerde Urtegård  
* Qingle Xu  


To get server setup run these commands in order
```
py –m virtualenv INFO212-Assignment4/
source INFO212-Assignment4/scripts/activate  
py -m pip install django  
py -m pip install djangorestframework  
cd mysite  
py manage.py makemigrations mysite
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

If you're not on Windows this probably works
```
python3 –m virtualenv INFO212-Assignment4/
source INFO212-Assignment4/bin/activate  
python3 -m pip install django  
python3 -m pip install djangorestframework  
cd mysite  
python3 manage.py makemigrations mysite
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```