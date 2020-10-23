# Django
This is a web application for snippets code which was created with Django Rest Framework. This application allows us to get, create, edit, and delete the snippets that were created with the logged-in user.
If the logged-in user has not any snippets created, it only can get all the created snippets and create new snippets.

## Getting Started
You need to run these commands from the terminal to config your environment.

```
virtualenv -p /usr/local/bin/python3 .
source bin/activate.fish
pip3 install django
pip3 install pygments
pip3 install djangorestframework
```

You can create a new user with this commands: 

```
python manage.py createsuperuser
```

## Run Application
Execute the following command for run-up the server.

```
cd mysite
python manage.py runserver
```

You can see the applications of snippets and admin opening in your browser the following:

Application: http://127.0.0.1:8000

Admin: http://127.0.0.1:8000/admin

python manage.py shell