# Unit II - Views and URLs

# WEB DEVELOPMENT IN PYTHON USING DJANGO

---

# Learning Objectives

After completing this unit, students will be able to:

- Understand Django Views.
- Create function-based views.
- Map URLs to views.
- Handle HTTP requests and responses.
- Pass parameters through URLs.
- Use regular expressions (or path converters) in URLs.
- Handle errors in Django applications.

---

# 1. Introduction to Views

## What is a View?

A **View** is a Python function or class that receives an HTTP request, performs the required business logic, and returns an HTTP response.

A view acts as the **controller** in Django's MVT architecture.

### Flow of a Request

```
Browser
   │
   ▼
URL
   │
   ▼
View
   │
   ▼
Template (Optional)
   │
   ▼
Response
```

---

## Responsibilities of a View

- Receive user requests.
- Process business logic.
- Retrieve data from the database.
- Send data to templates.
- Return an HTTP response.

---

# 2. Creating Views

Views are created inside the **views.py** file of an application.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django")
```

### Explanation

- `request` contains all information sent by the client.
- `HttpResponse()` sends data back to the browser.

---

## Multiple Views

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")
```

---

# 3. URL Mapping

## What is URL Mapping?

URL mapping connects a URL with a specific view.

Without URL mapping, Django does not know which view to execute.

---

## Project URLs

Open

```
project/urls.py
```

Example

```python
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
]
```

---

### URL Mapping Table

| URL | View Called |
|------|-------------|
| / | home() |
| /about/ | about() |
| /contact/ | contact() |

---

# 4. App-Level URLs

Instead of placing all URLs in the project, each app can have its own **urls.py**.

Example

```
student/
    urls.py
```

student/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
]
```

Project urls.py

```python
from django.urls import include, path

urlpatterns = [
    path('student/', include('student.urls')),
]
```

---

## Benefits of App-Level URLs

- Better organization
- Easy maintenance
- Suitable for large projects
- Reusable applications

---

# 5. View Logic

Views can perform calculations, process data, or interact with the database.

Example

```python
from django.http import HttpResponse

def square(request):
    number = 5
    result = number * number
    return HttpResponse(result)
```

Output

```
25
```

---

## Dynamic View

```python
from django.http import HttpResponse
import datetime

def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse(now)
```

Output

```
2026-07-24 11:30:00
```

---

# 6. HTTP Request

## What is an HTTP Request?

An HTTP Request is sent by the client (browser) to the server requesting a resource.

Examples

- Opening a webpage
- Logging in
- Submitting a form
- Downloading a file

---

## Request Flow

```
Client
   │
HTTP Request
   │
Server
   │
View
```

---

## Request Object

Every Django view receives a **request object**.

Example

```python
def home(request):
    pass
```

The request object contains:

- HTTP method
- User information
- Cookies
- Sessions
- Form data
- Uploaded files

---

## Common Request Attributes

| Attribute | Description |
|------------|-------------|
| request.method | Request type |
| request.GET | GET data |
| request.POST | POST data |
| request.user | Logged-in user |
| request.COOKIES | Cookies |
| request.session | Session data |

---

# 7. HTTP Methods

The most common HTTP methods are:

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Send data |
| PUT | Update data |
| DELETE | Delete data |

---

## GET Request

Used for reading data.

Example

```
https://example.com/search?name=Rahul
```

Accessing GET data

```python
def search(request):
    name = request.GET.get("name")
    return HttpResponse(name)
```

---

## POST Request

Used to submit sensitive data.

Example

```python
name = request.POST.get("name")
```

POST data is not displayed in the browser URL.

---

# 8. HTTP Response

## What is an HTTP Response?

A response is returned by the server after processing a request.

Example

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Students")
```

---

## Types of Responses

- HTML
- JSON
- Redirect
- File Download
- Plain Text

---

## Returning HTML

```python
return HttpResponse("<h1>Welcome</h1>")
```

Output

# Welcome

---

# 9. Rendering Templates

Instead of writing HTML inside a view, use templates.

Example

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

Advantages

- Clean code
- Easy maintenance
- Better separation of logic and presentation

---

# 10. URL Parameters

Django allows passing values through URLs.

Syntax

```python
path("hello/<str:name>/", views.hello)
```

View

```python
from django.http import HttpResponse

def hello(request, name):
    return HttpResponse("Hello " + name)
```

URL

```
/hello/Rahul/
```

Output

```
Hello Rahul
```

---

## Integer Parameter

URL

```python
path("square/<int:num>/", views.square)
```

View

```python
def square(request, num):
    return HttpResponse(num * num)
```

Input

```
/square/5/
```

Output

```
25
```

---

# 11. Path Converters

Django provides built-in path converters.

| Converter | Description |
|------------|-------------|
| str | String |
| int | Integer |
| slug | Slug value |
| uuid | UUID |
| path | Complete path |

Example

```python
path("student/<int:id>/", views.student)
```

---

# 12. Regular Expressions in URLs

Older versions of Django use **re_path()** for regular expressions.

Example

```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^student/[0-9]+/$', views.student),
]
```

This URL accepts only numbers.

Examples

Accepted

```
student/10/
student/100/
```

Rejected

```
student/abc/
```

---

## Another Example

```python
re_path(r'^year/[0-9]{4}/$', views.year)
```

Matches

```
year/2026/
```

---

# 13. Named URLs

Naming URLs makes templates easier to maintain.

Example

```python
path("about/", views.about, name="about")
```

Template

```html
<a href="{% url 'about' %}">About</a>
```

Benefits

- Easy maintenance
- No hardcoded URLs
- Better readability

---

# 14. URL Namespace

Useful when multiple apps have the same URL names.

student/urls.py

```python
app_name = "student"

urlpatterns = [
    path("", views.home, name="home"),
]
```

Template

```html
{% url 'student:home' %}
```

---

# 15. Error Handling

Errors occur when something goes wrong.

Common HTTP Errors

| Code | Meaning |
|------|----------|
| 200 | Success |
| 301 | Permanent Redirect |
| 302 | Temporary Redirect |
| 400 | Bad Request |
| 403 | Forbidden |
| 404 | Page Not Found |
| 500 | Internal Server Error |

---

## 404 Error

Occurs when a page is not found.

Example

```
http://localhost:8000/unknown/
```

Output

```
404 Page Not Found
```

---

## Custom 404 Page

Create

```
templates/404.html
```

Example

```html
<h1>Page Not Found</h1>
<p>The requested page does not exist.</p>
```

---

## 500 Error

Occurs due to server-side programming errors.

Example

```python
def test(request):
    x = 10 / 0
```

Output

```
500 Internal Server Error
```

---

# 16. Redirecting URLs

Use redirect() to send users to another page.

Example

```python
from django.shortcuts import redirect

def home(request):
    return redirect("/about/")
```

---

# 17. URL Resolution Process

```
User enters URL
        │
        ▼
Browser sends Request
        │
        ▼
urls.py checks URL
        │
        ▼
Matching View Found
        │
        ▼
View Executes
        │
        ▼
Response Returned
```

---

# Best Practices

- Keep views simple.
- Use app-level URLs.
- Use named URLs.
- Avoid writing HTML inside views.
- Handle errors properly.
- Organize URLs logically.
- Use path converters instead of complex regex whenever possible.

---

# Important Commands

Run Development Server

```bash
python manage.py runserver
```

Create App

```bash
python manage.py startapp student
```

---

# Frequently Asked Interview/Exam Questions

### Short Questions

1. What is a Django View?
2. Explain URL mapping.
3. What is the purpose of urls.py?
4. What is the request object?
5. Difference between GET and POST.
6. What is HttpResponse?
7. Explain URL parameters.
8. What are path converters?
9. What is re_path()?
10. Explain named URLs.
11. What is a 404 error?
12. Difference between render() and HttpResponse().
13. What is redirect()?
14. Explain app-level URL configuration.

---

# Unit II Summary

- Views contain the business logic of a Django application.
- URLs map browser requests to specific views.
- The `request` object stores request data such as GET, POST, cookies, and sessions.
- `HttpResponse` sends responses back to the client.
- Templates should be rendered using `render()`.
- URL parameters allow passing dynamic values to views.
- Path converters (`str`, `int`, `slug`, `uuid`, `path`) simplify URL handling.
- `re_path()` supports regular expression-based URL matching.
- Named URLs improve maintainability and avoid hardcoding.
- Django provides built-in support for handling HTTP errors such as 404 and 500.