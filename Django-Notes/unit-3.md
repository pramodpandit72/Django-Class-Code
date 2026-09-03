# Unit III - Templates, Debugging and Testing

# WEB DEVELOPMENT IN PYTHON USING DJANGO

---

# Learning Objectives

After completing this unit, students will be able to:

- Understand Django Templates.
- Create and use templates.
- Work with Django Template Language (DTL).
- Use template tags and variables.
- Implement loops and conditional statements.
- Create dynamic web pages.
- Use template inheritance.
- Debug Django applications.
- Perform testing in Django.

---

# 1. Introduction to Templates

## What is a Template?

A **Template** is an HTML file that displays data sent by a Django view.

Templates separate the **presentation layer (HTML)** from the **business logic (Python)**.

Instead of writing HTML inside views, Django recommends using templates.

---

## Why Use Templates?

- Separates HTML from Python code.
- Makes code easier to maintain.
- Supports reusable layouts.
- Generates dynamic web pages.
- Improves readability.

---

## Request-Response Flow

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
Template
   │
   ▼
HTML Response
```

---

# 2. Creating Templates

Create a folder named **templates** inside the project or app.

Example Project Structure

```
myproject/

│
├── student/
│
├── templates/
│      home.html
│      about.html
│
├── manage.py
```

---

## Configure Template Directory

Open **settings.py**

```python
'DIRS': [BASE_DIR / 'templates'],
```

This tells Django where to find template files.

---

## Creating First Template

home.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>

<h1>Welcome to Django</h1>

</body>
</html>
```

---

## Render Template

views.py

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

---

# 3. Django Template Language (DTL)

## What is DTL?

Django Template Language (DTL) is used to insert dynamic data into HTML pages.

It allows developers to use:

- Variables
- Tags
- Filters
- Loops
- Conditions

DTL does **not** allow direct execution of Python code for security reasons.

---

## DTL Syntax

| Syntax | Purpose |
|----------|----------|
| {{ }} | Variables |
| {% %} | Template Tags |
| {# #} | Comments |

---

# 4. Django Variables

Variables display values sent from views.

Example

views.py

```python
from django.shortcuts import render

def home(request):
    data = {
        "name": "Rahul"
    }
    return render(request, "home.html", data)
```

Template

```html
<h2>{{ name }}</h2>
```

Output

```
Rahul
```

---

## Multiple Variables

View

```python
data = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}
```

Template

```html
Name : {{ name }}

Age : {{ age }}

City : {{ city }}
```

Output

```
Name : Rahul

Age : 20

City : Delhi
```

---

# 5. Template Tags

Template tags perform logical operations.

Syntax

```html
{% tag %}
```

Common Tags

- if
- for
- include
- block
- extends
- url
- csrf_token

---

# 6. If Statement

Example

View

```python
data = {
    "marks": 80
}
```

Template

```html
{% if marks >= 40 %}
Pass
{% endif %}
```

Output

```
Pass
```

---

## If-Else Statement

```html
{% if marks >= 40 %}

Pass

{% else %}

Fail

{% endif %}
```

---

## If-Elif-Else

```html
{% if marks >= 90 %}

Excellent

{% elif marks >= 60 %}

Good

{% else %}

Average

{% endif %}
```

---

# 7. For Loop

Loops display multiple values.

View

```python
data = {
    "students": ["Rahul", "Aman", "Priya"]
}
```

Template

```html
<ul>

{% for student in students %}

<li>{{ student }}</li>

{% endfor %}

</ul>
```

Output

```
Rahul

Aman

Priya
```

---

## forloop Variables

| Variable | Meaning |
|------------|----------|
| forloop.counter | Starts from 1 |
| forloop.counter0 | Starts from 0 |
| forloop.first | First iteration |
| forloop.last | Last iteration |

Example

```html
{% for student in students %}

{{ forloop.counter }}. {{ student }}

{% endfor %}
```

Output

```
1. Rahul

2. Aman

3. Priya
```

---

# 8. Comments in Templates

```html
{# This is a comment #}
```

Comments are not displayed in the browser.

---

# 9. Template Filters

Filters modify variable values.

Syntax

```html
{{ variable|filter }}
```

---

## Common Filters

| Filter | Purpose |
|----------|----------|
| upper | Uppercase |
| lower | Lowercase |
| title | Title Case |
| length | Count items |
| default | Default value |
| truncatechars | Shorten text |

---

### upper

```html
{{ name|upper }}
```

Output

```
RAHUL
```

---

### lower

```html
{{ name|lower }}
```

Output

```
rahul
```

---

### title

```html
{{ name|title }}
```

Output

```
Rahul Kumar
```

---

### length

```html
{{ students|length }}
```

Output

```
3
```

---

### default

```html
{{ city|default:"Unknown" }}
```

---

# 10. Dynamic Templates

Dynamic templates display changing data from views.

View

```python
students = [
    "Rahul",
    "Priya",
    "Aman"
]

return render(request, "home.html", {
    "students": students
})
```

Template

```html
<h2>Student List</h2>

{% for student in students %}

<p>{{ student }}</p>

{% endfor %}
```

Every time data changes, the template updates automatically.

---

# 11. Template Inheritance

## What is Template Inheritance?

Template inheritance allows multiple pages to share a common layout.

It avoids code duplication.

---

## Base Template

base.html

```html
<!DOCTYPE html>

<html>

<head>

<title>Django</title>

</head>

<body>

<h1>My Website</h1>

{% block content %}

{% endblock %}

</body>

</html>
```

---

## Child Template

home.html

```html
{% extends "base.html" %}

{% block content %}

<h2>Welcome Students</h2>

{% endblock %}
```

Output

```
My Website

Welcome Students
```

---

## Advantages

- Reusable layout
- Less code duplication
- Easy maintenance
- Consistent design

---

# 12. include Tag

Used to include one template inside another.

header.html

```html
<h1>College Website</h1>
```

home.html

```html
{% include "header.html" %}
```

---

# 13. URL Tag

Generates URLs dynamically.

Example

```html
<a href="{% url 'about' %}">About</a>
```

Advantages

- No hardcoded URLs
- Easy maintenance

---

# 14. Debugging Django Applications

## What is Debugging?

Debugging is the process of finding and fixing errors in an application.

---

## Types of Errors

| Error | Description |
|----------|-------------|
| Syntax Error | Incorrect Python syntax |
| Runtime Error | Error during execution |
| Logical Error | Wrong program output |

---

## DEBUG Setting

Open **settings.py**

```python
DEBUG = True
```

When enabled, Django displays detailed error messages.

During deployment,

```python
DEBUG = False
```

---

## Common Debugging Techniques

- Read traceback carefully.
- Check syntax errors.
- Verify URLs.
- Check template names.
- Print variable values.
- Use browser developer tools.
- Verify database connections.

---

## Example

```python
print(name)
```

Console Output

```
Rahul
```

---

# 15. Common Template Errors

### Template Does Not Exist

Reason

- Wrong template path.

---

### Variable Not Displayed

Reason

- Variable not passed from view.

---

### URL Not Found

Reason

- Incorrect URL configuration.

---

### Syntax Error

Example

Wrong

```html
{{ name
```

Correct

```html
{{ name }}
```

---

# 16. Introduction to Testing

## What is Testing?

Testing checks whether an application works correctly.

It helps detect bugs before deployment.

---

## Advantages of Testing

- Finds errors early.
- Improves software quality.
- Makes maintenance easier.
- Increases reliability.
- Reduces development cost.

---

# 17. Django Testing

Testing code is written inside

```
tests.py
```

---

## Simple Test

tests.py

```python
from django.test import TestCase

class MyTest(TestCase):

    def test_addition(self):

        self.assertEqual(2 + 2, 4)
```

---

## Running Tests

Command

```bash
python manage.py test
```

Output

```
Ran 1 test

OK
```

---

# 18. Assertions

Assertions compare expected and actual values.

Common Assertions

| Assertion | Purpose |
|------------|----------|
| assertEqual() | Compare two values |
| assertTrue() | Check True |
| assertFalse() | Check False |
| assertIn() | Check value exists |
| assertNotEqual() | Compare inequality |

Example

```python
self.assertEqual(10, 10)
```

---

# 19. Testing Views

Example

```python
from django.test import TestCase
from django.urls import reverse

class ViewTest(TestCase):

    def test_home(self):

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
```

---

# Best Practices

- Keep HTML separate from Python code.
- Use template inheritance.
- Use variables instead of hardcoded values.
- Keep templates clean and organized.
- Use filters for formatting.
- Test applications regularly.
- Enable `DEBUG=True` only during development.

---

# Important Commands

Run Server

```bash
python manage.py runserver
```

Run Tests

```bash
python manage.py test
```

---

# Frequently Asked Interview/Exam Questions

### Short Questions

1. What is a Django Template?
2. Explain Django Template Language (DTL).
3. What is the purpose of `render()`?
4. Differentiate between variables and template tags.
5. Explain template inheritance.
6. What is the use of `{% extends %}`?
7. What is the use of `{% block %}`?
8. Explain the `for` loop in DTL.
9. Explain the `if-else` statement in templates.
10. What are template filters?
11. What is debugging?
12. What is the purpose of `DEBUG=True`?
13. Explain testing in Django.
14. What is `tests.py`?
15. Explain `assertEqual()`.

---

# Unit III Summary

- Templates are HTML files used to display dynamic content.
- Django Template Language (DTL) provides variables, tags, filters, and comments.
- Variables use `{{ }}` and tags use `{% %}`.
- `if`, `for`, and filters help create dynamic pages.
- Template inheritance (`extends` and `block`) promotes code reuse.
- `include` inserts reusable template fragments.
- Debugging helps identify and fix errors using tracebacks and the `DEBUG` setting.
- Testing ensures application correctness using `tests.py` and Django's built-in testing framework.