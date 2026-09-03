# Ultimate Django Commands Handbook

## Installation
```bash
python --version
pip --version
python -m pip install --upgrade pip
pip install django
pip install django==5.2
pip install --upgrade django
pip uninstall django
django-admin --version
python -m django --version
pip show django
pip list
```

## Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
deactivate
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Project & App
```bash
django-admin startproject myproject
django-admin startproject myproject .
cd myproject
python manage.py startapp appname
python manage.py runserver
python manage.py runserver 9000
python manage.py runserver 127.0.0.1:9000
python manage.py help
python manage.py check
python manage.py diffsettings
```

## Migrations
```bash
python manage.py makemigrations
python manage.py makemigrations appname
python manage.py makemigrations --merge
python manage.py makemigrations --empty appname
python manage.py migrate
python manage.py migrate appname
python manage.py migrate appname 0001
python manage.py migrate appname zero
python manage.py migrate --fake
python manage.py migrate --fake-initial
python manage.py migrate --plan
python manage.py showmigrations
python manage.py sqlmigrate appname 0001
```

## Database
```bash
python manage.py dbshell
python manage.py flush
python manage.py dumpdata > data.json
python manage.py loaddata data.json
```

## Admin & Users
```bash
python manage.py createsuperuser
python manage.py changepassword username
```

## Testing
```bash
python manage.py test
python manage.py test appname
```

## Static & Sessions
```bash
python manage.py collectstatic
python manage.py collectstatic --clear
python manage.py clearsessions
python manage.py createcachetable
```

# Common Imports
```python
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import path, include, re_path
from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
```

# ORM / QuerySet
```python
Model.objects.create()
Model.objects.all()
Model.objects.get()
Model.objects.filter()
Model.objects.exclude()
Model.objects.first()
Model.objects.last()
Model.objects.count()
Model.objects.exists()
Model.objects.order_by()
Model.objects.values()
Model.objects.values_list()
Model.objects.update()
Model.objects.delete()
Model.objects.get_or_create()
Model.objects.update_or_create()
Model.objects.bulk_create()
Model.objects.bulk_update()
Model.objects.aggregate()
Model.objects.annotate()
obj.save()
obj.delete()
```

# Forms
```python
form.is_valid()
form.cleaned_data
form.errors
form.save()
```

# Authentication
```python
authenticate()
login()
logout()
request.user
request.user.is_authenticated
@login_required
```

# Cookies
```python
response.set_cookie()
request.COOKIES.get()
response.delete_cookie()
```

# Sessions
```python
request.session["key"]="value"
request.session.get("key")
del request.session["key"]
request.session.flush()
request.session.clear()
request.session.keys()
request.session.items()
```

# Request
```python
request.method
request.GET
request.POST
request.FILES
request.COOKIES
request.session
request.user
request.path
request.headers
```

# Template Tags
```text
{{ }}
{% if %} {% elif %} {% else %} {% endif %}
{% for %} {% endfor %}
{% extends %}
{% block %} {% endblock %}
{% include %}
{% url %}
{% csrf_token %}
{# comment #}
```

# Filters
```text
upper
lower
title
length
default
truncatechars
date
safe
slice
join
```

# Model Fields
```text
AutoField
CharField
TextField
IntegerField
FloatField
BooleanField
DateField
DateTimeField
EmailField
FileField
ImageField
ForeignKey
OneToOneField
ManyToManyField
```

# Admin
```python
admin.site.register(Model)

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display=("id","name")
```
