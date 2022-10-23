Group 1 Oblig Group 2  
* Jakob Andreassen  
* Leander Giskegjerde Urtegård  
* Qingle Xu  


To get server setup run these commands in order
```
py –m virtualenv INFO212-Assignment4/
source Scripts/activate  
py -m pip install django  
py -m pip install djangorestframework  
cd mysite  
py manage.py createsuperuser
py manage.py makemigrations mysite
py manage.py migrate
py manage.py runserver
```