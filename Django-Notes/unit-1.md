# Unit I - Introduction to Django

# WEB DEVELOPMENT IN PYTHON USING DJANGO

---

# Learning Objectives

After completing this unit, students will be able to:

- Understand what Django is.
- Install Python and Django.
- Create a Django project.
- Understand project and app architecture.
- Use django-admin and manage.py commands.
- Create and manage Django applications.

---

# 1. Introduction to Django

## What is Django?

Django is a **high-level Python Web Framework** used for developing secure, scalable, and maintainable web applications quickly.

It follows the **MVT (Model-View-Template)** architecture.

Official Website:
https://www.djangoproject.com/

---

## Why Django?

Django provides many built-in features that reduce development time.

### Features

- Written in Python
- Open Source
- Fast Development
- Secure
- Scalable
- Built-in Admin Panel
- ORM (Object Relational Mapping)
- URL Routing
- Authentication System
- Template Engine

---

## Advantages of Django

- Rapid application development
- Less coding required
- High security
- Easy database connectivity
- Supports multiple databases
- Reusable applications
- Excellent documentation

---

## Applications of Django

Django is used for developing:

- E-commerce Websites
- Social Media Platforms
- Banking Applications
- Educational Portals
- Content Management Systems
- News Websites
- REST APIs
- Business Applications

Examples:

- Instagram (partially)
- Mozilla
- Pinterest (initial development)
- NASA
- Disqus

---

# 2. Installing Python

Download Python from:

https://python.org

### Verify Installation

Open Command Prompt:

```bash
python --version
```

or

```bash
python3 --version
```

Example Output

```
Python 3.12.1
```

---

# 3. Installing Django

Install Django using pip.

```bash
pip install django
```

Check installation

```bash
django-admin --version
```

Example
django-admin --version
```
5.2
```

Upgrade Django

```bash
pip install --upgrade django
```

---

# 4. Setting up Project in Editor

Recommended Editors

- VS Code
- PyCharm
- Sublime Text

Open terminal inside project folder.

Example

```bash
mkdir DjangoProjects
cd DjangoProjects
```

---

# 5. Creating Your First Django Project

Syntax

```bash
django-admin startproject projectname
```

Example

```bash
django-admin startproject myproject
```

Move into project

```bash
cd myproject
```

Run server

```bash
python manage.py runserver
```

Output

```
Starting development server...
```

Open Browser

```
http://127.0.0.1:8000/
```

If installation is correct, Django Welcome Page appears.

---

# 6. Project Structure

Example

```
myproject/
│
├── manage.py
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── db.sqlite3
```

---

## Explanation of Files

### manage.py

- Command-line utility
- Executes Django commands
- Used for running server, migrations etc.

Example

```bash
python manage.py runserver
```

---

### settings.py

Contains project settings.

Examples

- Installed Apps
- Database Configuration
- Middleware
- Templates
- Static Files
- Security Settings

---

### urls.py

Responsible for URL routing.

Example

```
/home
/about
/contact
```

---

### wsgi.py

Used for deployment using WSGI servers.

---

### asgi.py

Supports asynchronous applications.

---

### db.sqlite3

Default SQLite database.

---

# 7. Projects and Apps Overview

## What is a Project?

A project represents the complete website.

Example

```
College Management System
```

It may contain several apps.

---

## What is an App?

An app performs one specific functionality.

Examples

- Student App
- Faculty App
- Library App
- Attendance App
- Authentication App

---

## Difference Between Project and App

| Project | App |
|----------|-----|
| Complete website | Individual module |
| Contains settings | Contains business logic |
| Can have many apps | Belongs to one project |

---

# 8. Creating an App

Syntax

```bash
python manage.py startapp appname
```

Example

```bash
python manage.py startapp student
```

Project becomes

```
myproject/

student/

manage.py
```

---

# 9. App Structure

```
student/

│
├── migrations/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── __init__.py
```

---

## Explanation

### admin.py

Registers models for Admin Panel.

---

### apps.py

Stores application configuration.

---

### models.py

Contains database models.

---

### views.py

Contains business logic.

Receives request and returns response.

---

### tests.py

Used for testing.

---

### migrations/

Stores migration files.

---

# 10. Registering an App

Open

```
settings.py
```

Locate

```python
INSTALLED_APPS
```

Add

```python
INSTALLED_APPS = [
    ...
    'student',
]
```

---

# 11. Running Development Server

Command

```bash
python manage.py runserver
```

Custom Port

```bash
python manage.py runserver 9000
```

Example

```
http://127.0.0.1:9000
```

---

# 12. Django-admin Commands

| Command | Purpose |
|----------|----------|
| startproject | Create project |
| startapp | Create app |
| runserver | Start server |
| migrate | Apply migrations |
| makemigrations | Create migration |
| createsuperuser | Create admin user |
| shell | Open Python shell |
| test | Run tests |

---

# 13. Common manage.py Commands

Run Server

```bash
python manage.py runserver
```

Create App

```bash
python manage.py startapp student
```

Create Migrations

```bash
python manage.py makemigrations
```

Apply Migrations

```bash
python manage.py migrate
```

Create Admin User

```bash
python manage.py createsuperuser
```

Open Django Shell

```bash
python manage.py shell
```

Run Tests

```bash
python manage.py test
```

---

# 14. Django Development Workflow

```
Install Python

↓

Install Django

↓

Create Project

↓

Create App

↓

Register App

↓

Write Views

↓

Configure URLs

↓

Create Templates

↓

Run Server
```

---

# Important Interview/Exam Questions

### Short Questions

1. What is Django?
2. Explain MVT architecture.
3. What is manage.py?
4. Difference between Project and App.
5. Explain settings.py.
6. What is urls.py?
7. Explain app structure.
8. How do you create a Django project?
9. How do you create a Django app?
10. What is the purpose of admin.py?

---

# Important Commands Summary

```bash
pip install django

django-admin startproject myproject

cd myproject

python manage.py runserver

python manage.py startapp student

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py shell

python manage.py test
```

---

# Unit I Summary

- Django is a Python web framework.
- Django follows MVT architecture.
- Projects contain multiple apps.
- manage.py executes project commands.
- django-admin creates new projects.
- Apps contain models, views, admin, and tests.
- settings.py manages project configuration.
- urls.py manages URL routing.
- Django development begins with creating a project followed by creating apps.