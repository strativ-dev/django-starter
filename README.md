# Django Starter Project


This repository can be used to quickstart a django project.  


### List of packages added

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django CORS Header](https://github.com/adamchainz/django-cors-headers)
- [Django Environ](https://github.com/joke2k/django-environ)
- [Django Database URL](https://github.com/jacobian/dj-database-url)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Sendgrid](https://github.com/sendgrid/sendgrid-python)

### Packages for debugging/development purposes
- [Django Extension](https://github.com/django-extensions/django-extensions)
- [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)


### Packages for deploying in production
- [Gunicorn](https://gunicorn.org/)

### FYI
- For any other databases than `PostgreSQL`, remove `psycopg2` from `requirements.txt` and add necessary packages for that specific database


- `Django Extension` and `Django Debugger Tool` packages work only when DEBUG=True


- If you don't need to use `Django Rest Framwork` remove the package `djangorestframework` from `requirements.txt` file and remove `rest_framework` app from `INSTALLED_APPS`


- If you don't need to create APIs, you can remove `django-cors-headers` from `requirements.txt` and remove `CORS_ORIGIN_ALLOW_ALL`, `CORS_ALLOW_METHODS` and `CORS_ALLOW_HEADERS` from `settings.py`


- If you don't need to use `Sendgrid` for email remove it from `requirements.txt` .


### How to use

Clone the repository.

```sh
git clone git@github.com:strativ-dev/django-starter.git
```

Create and activate a virtual environment for the project.

For creating virtual environment we can use packages like [Virtualenv](https://pypi.org/project/virtualenv/) or [Pyenv](https://github.com/pyenv/pyenv). I've used Virtualenv.

```sh
cd django-starter
virtualenv venv
source venv/bin/activte
```
Install all required packages.

```sh
pip install -r requirements.txt # Required
pip install -r requirements.dev.txt # Only required for development
pip install -r requirements.prod.txt # Only required for production
```
Create a `.env` file copying from `.env.keep` file and update these values.
```env
# Comma separated hosts or IPs, set * to allow all 
ALLOWED_HOSTS=192.168.0.1,www.example.com 

# In production DEBUG should be False, in development it can be set to True
DEBUG=True 

# Secret key should be atleast 32 characters long and consists of alphanumeric and special characters
SECRET_KEY=**** 

# See django database URL documentation for other databases
DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME 

TEST_DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME

# Sendgrid single sender
SENDGRID_SENDER_EMAIL=username@email.com 

# Sendgrid API key
SENDGRID_API_KEY=****
```

<b>(Optional)</b> If you need to update the User model, do that now and after that run this command
```sh
python manage.py makemigrations
```

Run migrations.
```sh
python manage.py migrate
```

<b>(Optional)</b> Collect static files.
```sh
python manage.py collectstatic # To use this command you need to set DEBUG=False
```
Run the project.
```sh
python manage.py runserver
```
