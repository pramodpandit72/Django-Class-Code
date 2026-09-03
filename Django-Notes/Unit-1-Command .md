# Django Commands – Introduction to Django

## 1. Check Python Version

```bash
python --version
```

**Use:** Displays the installed Python version.

---

## 2. Check pip Version

```bash
pip --version
```

**Use:** Displays the installed pip version.

---

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

**Use:** Updates pip to the latest version.

---

## 4. Install Django

```bash
pip install django
```

**Use:** Installs the latest Django framework.

---

## 5. Install Specific Django Version

```bash
pip install django==5.0
```

**Use:** Installs a specific version of Django.

---

## 6. Check Django Version

```bash
django-admin --version
```

**Use:** Displays the installed Django version.

---

## 7. Show Installed Packages

```bash
pip list
```

**Use:** Lists all installed Python packages.

---

## 8. Show Django Package Information

```bash
pip show django
```

**Use:** Displays detailed information about the installed Django package.

---

## 9. Uninstall Django

```bash
pip uninstall django
```

**Use:** Removes Django from the system.

---

## 10. Create Virtual Environment

```bash
python -m venv env
```

**Use:** Creates a virtual environment named `env`.

---

## 11. Activate Virtual Environment (Windows)

```bash
env\Scripts\activate
```

**Use:** Activates the virtual environment.

---

## 12. Activate Virtual Environment (Linux/macOS)

```bash
source env/bin/activate
```

**Use:** Activates the virtual environment.

---

## 13. Deactivate Virtual Environment

```bash
deactivate
```

**Use:** Exits the virtual environment.

---

## 14. Open Project in VS Code

```bash
code .
```

**Use:** Opens the current folder in Visual Studio Code.

---

## 15. Create a Django Project

```bash
django-admin startproject project_name
```

**Use:** Creates a new Django project.

---

## 16. Move into Project Directory

```bash
cd project_name
```

**Use:** Changes the current directory to the project folder.

---

## 17. Start Development Server

```bash
python manage.py runserver
```

**Use:** Starts the Django development server.

---

## 18. Start Server on Custom Port

```bash
python manage.py runserver 8001
```

**Use:** Starts the development server on port `8001`.

---

## 19. Start Server on Specific IP and Port

```bash
python manage.py runserver 0.0.0.0:8000
```

**Use:** Makes the development server accessible on the local network.

---

## 20. Create a Django App

```bash
python manage.py startapp app_name
```

**Use:** Creates a new Django application inside the project.

---

## 21. Check Project for Errors

```bash
python manage.py check
```

**Use:** Checks the project for configuration issues.

---

## 22. Create Migration Files

```bash
python manage.py makemigrations
```

**Use:** Creates migration files based on model changes.

---

## 23. Apply Migrations

```bash
python manage.py migrate
```

**Use:** Applies migrations to the database.

---

## 24. Show Migration Status

```bash
python manage.py showmigrations
```

**Use:** Displays applied and pending migrations.

---

## 25. Open Django Shell

```bash
python manage.py shell
```

**Use:** Opens the interactive Django shell.

---

## 26. Create Superuser

```bash
python manage.py createsuperuser
```

**Use:** Creates an administrator account for the Django Admin Panel.

---

## 27. Change User Password

```bash
python manage.py changepassword username
```

**Use:** Changes the password of an existing user.

---

## 28. Collect Static Files

```bash
python manage.py collectstatic
```

**Use:** Collects all static files into a single directory for deployment.

---

## 29. Run Test Cases

```bash
python manage.py test
```

**Use:** Runs all test cases in the project.

---

## 30. Display Help for manage.py Commands

```bash
python manage.py help
```

**Use:** Lists all available `manage.py` commands.

---

## 31. Display Help for django-admin Commands

```bash
django-admin help
```

**Use:** Lists all available `django-admin` commands.