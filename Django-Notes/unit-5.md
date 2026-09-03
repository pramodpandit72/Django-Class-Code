# Unit V - Models, Migrations and Django Admin

# WEB DEVELOPMENT IN PYTHON USING DJANGO

---

# Learning Objectives

After completing this unit, students will be able to:

- Understand Django Models.
- Create database models.
- Work with migrations.
- Perform CRUD operations using Django Shell.
- Understand Object Relational Mapping (ORM).
- Create relationships using Foreign Keys.
- Work with Django Admin.
- Manage users and groups.
- Configure database connections.

---

# 1. Introduction to Models

## What is a Model?

A **Model** is a Python class that represents a database table.

Each model contains fields that correspond to columns in the database.

Example

```
Student Table

ID    Name      Age

1     Rahul     20

2     Aman      21
```

In Django, the above table is represented by a model.

---

## Why Use Models?

- Represent database tables.
- Store application data.
- Simplify database operations.
- Work with databases using Python code.
- Eliminate the need to write SQL queries.

---

# 2. Creating Models

Models are created inside **models.py**.

Example

```python
from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    age = models.IntegerField()

    email = models.EmailField()

    def __str__(self):
        return self.name
```

---

## Explanation

| Field | Description |
|--------|-------------|
| CharField | Stores text |
| IntegerField | Stores integers |
| EmailField | Stores email addresses |
| __str__() | Returns readable object name |

---

# 3. Common Model Fields

| Field | Purpose |
|--------|----------|
| CharField | Text |
| TextField | Large text |
| IntegerField | Integer values |
| FloatField | Decimal numbers |
| BooleanField | True or False |
| DateField | Date |
| DateTimeField | Date and Time |
| EmailField | Email |
| ImageField | Images |
| FileField | Files |
| ForeignKey | One-to-Many Relationship |

---

# 4. Migrations

## What is Migration?

Migration is the process of applying changes made in models to the database.

Whenever a model is created or modified, Django generates migration files.

---

## Migration Workflow

```
Create Model

↓

makemigrations

↓

Migration File

↓

migrate

↓

Database Updated
```

---

# 5. Creating Migrations

Command

```bash
python manage.py makemigrations
```

Example Output

```
Migrations for 'student'

0001_initial.py
```

---

# 6. Applying Migrations

Command

```bash
python manage.py migrate
```

Output

```
Applying student.0001_initial... OK
```

---

# 7. Viewing Migration Status

Command

```bash
python manage.py showmigrations
```

Example

```
student

[X] 0001_initial
```

`[X]` indicates that the migration has been applied.

---

# 8. Django Shell

## What is Django Shell?

Django Shell is an interactive Python environment used to work with models.

Open Shell

```bash
python manage.py shell
```

---

# 9. Insert Data

Example

```python
from student.models import Student

s = Student(
    name="Rahul",
    age=20,
    email="rahul@gmail.com"
)

s.save()
```

Another Example

```python
Student.objects.create(
    name="Aman",
    age=22,
    email="aman@gmail.com"
)
```

---

# 10. Retrieve Data

Retrieve All Records

```python
Student.objects.all()
```

Retrieve One Record

```python
Student.objects.get(id=1)
```

Retrieve Using Filter

```python
Student.objects.filter(age=20)
```

---

# 11. Update Data

Example

```python
student = Student.objects.get(id=1)

student.age = 25

student.save()
```

---

# 12. Delete Data

Delete One Record

```python
student = Student.objects.get(id=1)

student.delete()
```

Delete Multiple Records

```python
Student.objects.filter(age=20).delete()
```

---

# 13. CRUD Operations

CRUD stands for:

| Operation | Meaning |
|------------|----------|
| Create | Insert Data |
| Read | Retrieve Data |
| Update | Modify Data |
| Delete | Remove Data |

---

# 14. Object Relational Mapping (ORM)

## What is ORM?

ORM (Object Relational Mapping) is a technique that allows developers to interact with the database using Python objects instead of SQL queries.

---

## Without ORM

```sql
SELECT * FROM Student;
```

---

## With ORM

```python
Student.objects.all()
```

---

## Advantages of ORM

- No SQL knowledge required.
- Portable across databases.
- Secure against SQL Injection.
- Easy to maintain.
- Faster development.

---

# 15. Common ORM Methods

| Method | Purpose |
|----------|----------|
| all() | Retrieve all records |
| get() | Retrieve one record |
| filter() | Retrieve matching records |
| create() | Insert data |
| save() | Save object |
| delete() | Delete object |
| update() | Update records |
| count() | Count records |
| first() | First record |
| last() | Last record |

---

## Example

```python
Student.objects.count()
```

Output

```
5
```

---

# 16. Foreign Keys

## What is a Foreign Key?

A **Foreign Key** creates a **One-to-Many relationship** between two tables.

Example

One Department has many Students.

---

## Example Model

```python
class Department(models.Model):

    name = models.CharField(max_length=100)
```

```python
class Student(models.Model):

    name = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
```

---

## Relationship Diagram

```
Department

ID   Name

1    CSE

2    ECE

        ▲

        │

Student

ID   Name     Department

1    Rahul       1

2    Aman        1

3    Priya       2
```

---

## on_delete Options

| Option | Meaning |
|----------|----------|
| CASCADE | Delete child records automatically |
| SET_NULL | Set value to NULL |
| PROTECT | Prevent deletion |
| SET_DEFAULT | Set default value |

---

# 17. Django Admin

## What is Django Admin?

Django Admin is a built-in web interface used to manage application data.

---

## Create Superuser

Command

```bash
python manage.py createsuperuser
```

Example

```
Username

Email

Password
```

---

## Run Server

```bash
python manage.py runserver
```

Admin URL

```
http://127.0.0.1:8000/admin/
```

---

# 18. Register Models

Open **admin.py**

```python
from django.contrib import admin

from .models import Student

admin.site.register(Student)
```

Now the Student model appears in the Admin Panel.

---

# 19. Django Admin Features

- Add records
- Edit records
- Delete records
- Search data
- Filter data
- Manage users
- Manage groups

---

# 20. Users and Groups

## User

A user is an individual who can log in to the application.

Examples

- Administrator
- Teacher
- Student

---

## Group

A group is a collection of users having similar permissions.

Example

```
Teachers

↓

Add Student

Edit Student

View Student
```

---

# 21. Permissions

Permissions control user access.

Default Permissions

- Add
- Change
- Delete
- View

Example

Teacher

✔ View

✔ Change

❌ Delete

---

# 22. Database Configuration

Django stores database settings inside **settings.py**.

Default Database

```python
DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",

    }

}
```

---

# 23. Using MySQL

Example Configuration

```python
DATABASES = {

    "default": {

        "ENGINE":
        "django.db.backends.mysql",

        "NAME": "college",

        "USER": "root",

        "PASSWORD": "root",

        "HOST": "localhost",

        "PORT": "3306",

    }

}
```

---

# 24. Supported Databases

| Database | Supported |
|-----------|-----------|
| SQLite | Yes |
| MySQL | Yes |
| PostgreSQL | Yes |
| Oracle | Yes |
| MariaDB | Yes |

---

# 25. Model Lifecycle

```
Create Model

↓

makemigrations

↓

migrate

↓

Insert Data

↓

Retrieve Data

↓

Update Data

↓

Delete Data
```

---

# Best Practices

- Use meaningful model names.
- Always run migrations after changing models.
- Prefer ORM over raw SQL.
- Register models in `admin.py`.
- Use Foreign Keys for relationships.
- Create strong passwords for admin users.
- Grant only necessary permissions.

---

# Important Commands

Create Migration

```bash
python manage.py makemigrations
```

Apply Migration

```bash
python manage.py migrate
```

Open Shell

```bash
python manage.py shell
```

Create Superuser

```bash
python manage.py createsuperuser
```

View Migrations

```bash
python manage.py showmigrations
```

Run Server

```bash
python manage.py runserver
```

---

# Frequently Asked Interview/Exam Questions

### Short Questions

1. What is a Django Model?
2. Explain migrations.
3. Difference between `makemigrations` and `migrate`.
4. What is Django Shell?
5. Explain CRUD operations.
6. What is ORM?
7. Advantages of ORM.
8. Explain `save()` and `delete()`.
9. What is a Foreign Key?
10. Explain `on_delete=models.CASCADE`.
11. What is Django Admin?
12. How do you create a superuser?
13. What are Groups?
14. Explain Permissions.
15. How is the database configured in Django?

---

# Unit V Summary

- Models represent database tables in Django.
- Migrations synchronize model changes with the database.
- Django Shell allows developers to perform CRUD operations interactively.
- ORM enables database interaction using Python instead of SQL.
- Foreign Keys establish relationships between tables.
- Django Admin provides a built-in interface to manage application data.
- Users, Groups, and Permissions help implement access control.
- Database settings are configured in `settings.py`, and Django supports multiple database systems such as SQLite, MySQL, and PostgreSQL.