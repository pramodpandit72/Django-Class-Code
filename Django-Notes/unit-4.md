# Unit IV - Forms in Django

# WEB DEVELOPMENT IN PYTHON USING DJANGO

---

# Learning Objectives

After completing this unit, students will be able to:

- Understand Django Forms.
- Differentiate between GET and POST methods.
- Build forms using Django.
- Understand Cross Site Request Forgery (CSRF).
- Implement CSRF protection.
- Perform POST-Redirect-GET (PRG).
- Validate user input using Django Forms.

---

# 1. Introduction to Forms

## What is a Form?

A **Form** is used to collect data from users and send it to the server for processing.

Examples:

- Login Form
- Registration Form
- Contact Form
- Feedback Form
- Student Admission Form

---

## Why Use Django Forms?

Django Forms provide:

- Easy form creation
- Automatic validation
- Secure data handling
- Protection against common attacks
- Reduced coding effort

---

## Form Processing Flow

```
User
   │
   ▼
Fill Form
   │
   ▼
Submit
   │
   ▼
View
   │
   ▼
Validation
   │
   ▼
Database / Response
```

---

# 2. HTTP Methods

Forms mainly use two HTTP methods:

- GET
- POST

---

## GET Method

### Definition

The GET method sends data through the URL.

Example

```
http://localhost:8000/search/?name=Rahul
```

---

### Characteristics of GET

- Data visible in URL
- Limited data size
- Can be bookmarked
- Used for searching and retrieving data

---

### HTML Example

```html
<form method="GET">

<input type="text" name="name">

<input type="submit">

</form>
```

---

### Accessing GET Data

```python
def search(request):

    name = request.GET.get("name")

    return HttpResponse(name)
```

---

## Advantages of GET

- Faster
- Easy to bookmark
- Suitable for searching
- Simple implementation

---

## Disadvantages of GET

- Data visible in URL
- Less secure
- Not suitable for passwords
- Limited data length

---

# 3. POST Method

## Definition

The POST method sends data inside the request body.

The submitted data is **not visible in the URL**.

---

### HTML Example

```html
<form method="POST">

{% csrf_token %}

<input type="text" name="name">

<input type="submit">

</form>
```

---

### Accessing POST Data

```python
def home(request):

    name = request.POST.get("name")

    return HttpResponse(name)
```

---

## Advantages of POST

- Secure
- Large amount of data
- Suitable for passwords
- Supports file uploads

---

## Disadvantages

- Cannot be bookmarked
- Slightly slower than GET
- Requires CSRF protection

---

# 4. Difference Between GET and POST

| GET | POST |
|------|------|
| Retrieves data | Sends data |
| Data visible in URL | Data hidden |
| Less secure | More secure |
| Limited data | Large data |
| Bookmark supported | Bookmark not supported |
| Used for search | Used for forms |

---

# 5. Building Forms Using Django

Django provides a **forms** module to build forms easily.

---

## Step 1: Create forms.py

Inside the application

```
student/

forms.py
```

---

## Step 2: Import Forms

```python
from django import forms
```

---

## Step 3: Create Form

```python
from django import forms

class StudentForm(forms.Form):

    name = forms.CharField(max_length=100)

    age = forms.IntegerField()

    email = forms.EmailField()
```

---

## Step 4: Create View

```python
from django.shortcuts import render

from .forms import StudentForm

def student(request):

    form = StudentForm()

    return render(request, "student.html",
    {"form": form})
```

---

## Step 5: Create Template

```html
<form method="POST">

{% csrf_token %}

{{ form.as_p }}

<input type="submit">

</form>
```

---

### Form Display Methods

| Method | Output |
|----------|---------|
| form.as_p | Paragraph format |
| form.as_table | Table format |
| form.as_ul | List format |

---

# 6. Form Submission

Example View

```python
from django.shortcuts import render

from .forms import StudentForm

def student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

    else:

        form = StudentForm()

    return render(request,
                  "student.html",
                  {"form": form})
```

---

# 7. Checking Request Method

```python
if request.method == "POST":

    print("Form Submitted")

else:

    print("Page Loaded")
```

---

# 8. Cross Site Request Forgery (CSRF)

## What is CSRF?

**Cross Site Request Forgery (CSRF)** is a security attack in which an attacker tricks a logged-in user into performing unwanted actions on a website without their consent.

---

## Example

Suppose a user is logged into an online banking website.

A malicious website silently sends a request to transfer money.

Without CSRF protection, the bank may treat the request as valid.

---

## CSRF Protection in Django

Django protects POST requests using a **CSRF Token**.

Every POST form must contain:

```html
{% csrf_token %}
```

---

## Example

```html
<form method="POST">

{% csrf_token %}

<input type="text" name="name">

<input type="submit">

</form>
```

---

## Without CSRF Token

Django returns:

```
403 Forbidden
```

Error Message

```
CSRF verification failed.
```

---

## Advantages of CSRF Protection

- Prevents unauthorized requests
- Protects user accounts
- Improves website security
- Enabled by default in Django

---

# 9. Implementing POST Redirect GET (PRG)

## What is PRG?

PRG stands for:

```
POST

↓

Redirect

↓

GET
```

It prevents duplicate form submissions when the user refreshes the page.

---

## Without PRG

```
Fill Form

↓

Submit

↓

Refresh

↓

Form Submitted Again
```

---

## With PRG

```
Fill Form

↓

POST

↓

Redirect

↓

GET

↓

Safe Refresh
```

---

## Example

```python
from django.shortcuts import redirect

def student(request):

    if request.method == "POST":

        return redirect("success")

    return render(request,
                  "student.html")
```

---

## Advantages of PRG

- Prevents duplicate submissions
- Better user experience
- Safe page refresh
- Avoids repeated database inserts

---

# 10. Data Validation

## What is Validation?

Validation checks whether user input is correct before processing.

Example

- Name should not be empty.
- Age must be positive.
- Email must be valid.

---

## Built-in Validation

```python
class StudentForm(forms.Form):

    name = forms.CharField(max_length=100)

    age = forms.IntegerField()

    email = forms.EmailField()
```

---

## Checking Validity

```python
if form.is_valid():

    print("Valid Data")
```

---

## Complete Example

```python
def student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            return HttpResponse("Success")

    else:

        form = StudentForm()

    return render(request,
                  "student.html",
                  {"form": form})
```

---

# 11. Accessing Validated Data

```python
if form.is_valid():

    name = form.cleaned_data["name"]

    age = form.cleaned_data["age"]

    email = form.cleaned_data["email"]
```

`cleaned_data` contains validated user input.

---

# 12. Validation Errors

Example

```python
if not form.is_valid():

    print(form.errors)
```

Output

```
This field is required.
```

---

# 13. Custom Validation

Example

```python
from django import forms

class StudentForm(forms.Form):

    age = forms.IntegerField()

    def clean_age(self):

        age = self.cleaned_data["age"]

        if age < 18:

            raise forms.ValidationError(
                "Age must be at least 18."
            )

        return age
```

---

# 14. Common Form Fields

| Field | Purpose |
|--------|----------|
| CharField | Text input |
| IntegerField | Numbers |
| FloatField | Decimal values |
| EmailField | Email validation |
| BooleanField | Checkbox |
| DateField | Date input |
| ChoiceField | Dropdown list |
| FileField | File upload |
| ImageField | Image upload |

---

# 15. Form Widgets

Widgets control the appearance of form fields.

Example

```python
name = forms.CharField(
    widget=forms.TextInput()
)
```

---

## Common Widgets

| Widget | Purpose |
|----------|----------|
| TextInput | Text box |
| PasswordInput | Password |
| EmailInput | Email |
| Textarea | Multi-line text |
| CheckboxInput | Checkbox |
| Select | Dropdown |

---

# 16. File Upload Forms (Introduction)

Example

```python
class UploadForm(forms.Form):

    file = forms.FileField()
```

HTML

```html
<form method="POST"
      enctype="multipart/form-data">

{% csrf_token %}

{{ form.as_p }}

<input type="submit">

</form>
```

---

# Best Practices

- Use Django Forms instead of plain HTML forms whenever possible.
- Use POST for sensitive data.
- Always include `{% csrf_token %}` in POST forms.
- Validate all user inputs.
- Use PRG to prevent duplicate submissions.
- Display validation errors to users.

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

1. What is a Django Form?
2. Explain GET and POST methods.
3. Differentiate between GET and POST.
4. What is CSRF?
5. Why is `{% csrf_token %}` required?
6. What is POST Redirect GET (PRG)?
7. What is validation?
8. Explain `form.is_valid()`.
9. What is `cleaned_data`?
10. What is `forms.py`?
11. Explain custom validation.
12. What are widgets in Django Forms?
13. Name any five built-in form fields.

---

# Unit IV Summary

- Django Forms simplify form creation and validation.
- GET is used for retrieving data, while POST is used for submitting data securely.
- POST requests should always include a CSRF token.
- Django provides built-in validation through `is_valid()`.
- `cleaned_data` stores validated form data.
- Custom validation can be implemented using `clean_<fieldname>()` methods.
- POST-Redirect-GET (PRG) prevents duplicate form submissions.
- Widgets customize the appearance of form fields.
- Django Forms improve security, maintainability, and user experience.