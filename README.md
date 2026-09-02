# Django Class Code

A beginner-friendly Django project that demonstrates core web development concepts such as URL routing, function-based views, dynamic route parameters, query parameters, templates, template inheritance, regular-expression routes, and basic error handling.

## Overview

This repository contains a Django project named `myproject` with one application, `myapp`. It is designed as classroom practice code for learning how Django handles requests, renders responses, maps URLs to views, and works with HTML templates.

## Features

- Function-based Django views
- Static and dynamic URL routing
- Query parameter handling
- Regular-expression URL patterns
- HTML responses using `HttpResponse`
- Template rendering with Django templates
- Template inheritance examples
- Basic arithmetic and student/menu examples
- Custom 404 and 500 error handler configuration
- SQLite database configuration for local development

## Project Structure

```text
.
|-- myproject/
|   |-- manage.py
|   |-- myproject/
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- views.py
|   |   |-- asgi.py
|   |   `-- wsgi.py
|   `-- myapp/
|       |-- views.py
|       |-- urls.py
|       |-- models.py
|       |-- admin.py
|       |-- templates/
|       `-- template1/
|-- requirements.txt
`-- README.md
```

## Requirements

- Python 3.12 or newer
- Django 6.1
- pip

Project dependencies are listed in `requirements.txt`.

## Setup Instructions

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create and activate a virtual environment:

```bash
python -m venv myenv
```

On Windows:

```bash
myenv\Scripts\activate
```

On macOS/Linux:

```bash
source myenv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Move into the Django project directory:

```bash
cd myproject
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open the project in your browser:

```text
http://127.0.0.1:8000/
```

## Useful Routes

| Route | Description |
| --- | --- |
| `/hello/` | Displays a simple Hello World response |
| `/home/` | Displays a basic home page response |
| `/curr_time/` | Shows the current server time |
| `/dish/` | Displays a single menu item |
| `/dishes/` | Displays multiple menu items |
| `/greet/<name>` | Greets the user using a route parameter |
| `/recipe/?food=cake` | Reads a query parameter |
| `/addition/?value1=10&value2=5` | Adds two query parameter values |
| `/calculate/?operation=add&value1=10&value2=5` | Performs a calculation |
| `/home1/` | Renders a template-based home page |
| `/about/` | Renders an about page |
| `/menu/` | Renders a menu template with context data |
| `/menu1/` | Renders a menu list using template data |
| `/admin/` | Opens the Django admin panel |

## Example Query URLs

```text
http://127.0.0.1:8000/recipe/?food=pizza
http://127.0.0.1:8000/addition/?value1=20&value2=30
http://127.0.0.1:8000/calculate/?operation=multiply&value1=5&value2=4
```

## Development Notes

- Main URL configuration is available in `myproject/myproject/urls.py`.
- App-level routes are available in `myproject/myapp/urls.py`.
- Most examples are implemented in `myproject/myapp/views.py`.
- Templates are stored in `myproject/myapp/templates/` and `myproject/myapp/template1/`.
- The project uses SQLite by default.

## Running Tests

Run the Django test suite from the `myproject` directory:

```bash
python manage.py test
```

## Security Notes

This project is intended for learning and local development. Before deploying to production:

- Set a secure `DJANGO_SECRET_KEY` environment variable.
- Set `DEBUG = False`.
- Replace `ALLOWED_HOSTS = ["*"]` with specific allowed domains.
- Review Django's deployment checklist.

## Author

Created as part of Django classroom practice and learning exercises.
