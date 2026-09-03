# Unit VI - Cookies, Sessions, Users and Authentication

# WEB DEVELOPMENT IN PYTHON USING DJANGO

---

# Learning Objectives

After completing this unit, students will be able to:

- Understand Cookies and Sessions.
- Create and manage Cookies in Django.
- Create and manage Sessions in Django.
- Create and manage Users.
- Implement Login and Logout.
- Use Django Authentication in Views.

---

# 1. Introduction to Cookies

## What is a Cookie?

A **Cookie** is a small piece of data stored in the user's web browser by the server.

Cookies are used to remember information about the user between requests.

---

## Why are Cookies Used?

Cookies help in:

- Remembering user preferences
- Saving login information
- Tracking user activity
- Personalizing websites
- Maintaining shopping carts

---

## Cookie Flow

```
Client (Browser)
      │
      │ Request
      ▼
Server
      │
      │ Set Cookie
      ▼
Browser Stores Cookie
      │
      │ Sends Cookie in Next Request
      ▼
Server Reads Cookie
```

---

## Characteristics of Cookies

- Stored in the browser.
- Small in size (about 4 KB).
- Can have an expiry date.
- Sent automatically with every request to the same website.

---

# 2. Creating Cookies in Django

Use the **set_cookie()** method.

Example

```python
from django.http import HttpResponse

def set_cookie(request):

    response = HttpResponse("Cookie Created")

    response.set_cookie("username", "Rahul")

    return response
```

---

# 3. Reading Cookies

Example

```python
from django.http import HttpResponse

def get_cookie(request):

    name = request.COOKIES.get("username")

    return HttpResponse(name)
```

Output

```
Rahul
```

---

# 4. Deleting Cookies

Example

```python
from django.http import HttpResponse

def delete_cookie(request):

    response = HttpResponse("Cookie Deleted")

    response.delete_cookie("username")

    return response
```

---

# 5. Setting Cookie Expiry

Example

```python
response.set_cookie(
    "username",
    "Rahul",
    max_age=3600
)
```

- `max_age=3600` means the cookie expires after **1 hour**.

---

# 6. Advantages and Disadvantages of Cookies

### Advantages

- Easy to implement.
- Improves user experience.
- Stores user preferences.
- Reduces repeated data entry.

### Disadvantages

- Limited storage capacity.
- Can be modified by users.
- Less secure for sensitive data.
- Stored on the client side.

---

# 7. Introduction to Sessions

## What is a Session?

A **Session** stores user information on the **server** instead of the browser.

The browser stores only a **Session ID**, while the actual data remains secure on the server.

---

## Why Use Sessions?

Sessions are used for:

- User login
- Shopping carts
- User authentication
- Temporary user data
- Secure data storage

---

## Session Flow

```
User Logs In
      │
      ▼
Server Creates Session
      │
      ▼
Session ID Sent to Browser
      │
      ▼
Browser Sends Session ID
      │
      ▼
Server Retrieves Session Data
```

---

# 8. Creating Sessions

Example

```python
def login(request):

    request.session["username"] = "Rahul"

    return HttpResponse("Session Created")
```

---

# 9. Reading Sessions

Example

```python
def profile(request):

    username = request.session.get("username")

    return HttpResponse(username)
```

Output

```
Rahul
```

---

# 10. Deleting Sessions

Delete a single session value

```python
del request.session["username"]
```

---

## Delete Entire Session

```python
request.session.flush()
```

This removes all session data.

---

# 11. Difference Between Cookies and Sessions

| Cookies | Sessions |
|----------|----------|
| Stored in browser | Stored on server |
| Less secure | More secure |
| Limited size | Larger storage |
| Can be modified by user | Cannot be directly modified by user |
| Used for preferences | Used for login and authentication |

---

# 12. Users in Django

## What is a User?

A **User** is a person who can access the Django application.

Examples

- Administrator
- Student
- Teacher
- Employee

---

## User Information

Each user contains:

- Username
- Password
- Email
- First Name
- Last Name

---

# 13. Creating Users

### Method 1: Using Admin Panel

```
Admin Panel

↓

Users

↓

Add User
```

---

### Method 2: Using Shell

Open Shell

```bash
python manage.py shell
```

Example

```python
from django.contrib.auth.models import User

User.objects.create_user(

    username="rahul",

    password="rahul123"

)
```

---

# 14. Django Authentication

## What is Authentication?

**Authentication** is the process of verifying the identity of a user.

Example

```
Username

Password

↓

Login Successful
```

---

## Authentication Process

```
Login Form

↓

Username & Password

↓

Authentication

↓

Valid User

↓

Access Granted
```

---

# 15. Login View

Example

```python
from django.contrib.auth import authenticate
from django.contrib.auth import login

def user_login(request):

    user = authenticate(

        username="rahul",

        password="rahul123"

    )

    if user is not None:

        login(request, user)

        return HttpResponse("Login Successful")

    return HttpResponse("Invalid Credentials")
```

---

## Explanation

- `authenticate()` checks username and password.
- `login()` creates a session for the authenticated user.

---

# 16. Logout View

Example

```python
from django.contrib.auth import logout

def user_logout(request):

    logout(request)

    return HttpResponse("Logged Out")
```

---

# 17. Login and Logout URLs

Project **urls.py**

```python
from django.urls import path

from . import views

urlpatterns = [

    path("login/", views.user_login, name="login"),

    path("logout/", views.user_logout, name="logout"),

]
```

---

# 18. Login Form Example

```html
<form method="POST">

{% csrf_token %}

<input
type="text"
name="username"
placeholder="Username">

<input
type="password"
name="password"
placeholder="Password">

<input
type="submit"
value="Login">

</form>
```

---

# 19. Login Using User Input

Example

```python
from django.contrib.auth import authenticate
from django.contrib.auth import login

def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None:

            login(request, user)

            return HttpResponse("Login Successful")

    return HttpResponse("Invalid Credentials")
```

---

# 20. Using Login in Views

Some pages should be accessible only after login.

Example

```python
from django.http import HttpResponse

def dashboard(request):

    if request.user.is_authenticated:

        return HttpResponse("Welcome")

    return HttpResponse("Please Login")
```

---

# 21. Login Required Decorator

Django provides the `login_required` decorator to restrict access.

Example

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    return HttpResponse("Dashboard")
```

If the user is not logged in, Django redirects to the login page.

---

# 22. Checking Authentication Status

Example

```python
if request.user.is_authenticated:

    print("Logged In")

else:

    print("Anonymous User")
```

---

# 23. Changing Password

Example

```python
user.set_password("newpassword")

user.save()
```

---

# 24. Best Practices for Authentication

- Use strong passwords.
- Store passwords securely (Django hashes passwords automatically).
- Never save plain-text passwords.
- Use sessions for authenticated users.
- Always use CSRF protection in login forms.
- Log users out after sensitive operations if necessary.

---

# 25. Complete Authentication Flow

```
User Opens Login Page

↓

Enters Username & Password

↓

authenticate()

↓

Valid User?

↓

Yes

↓

login()

↓

Session Created

↓

Access Protected Pages

↓

logout()

↓

Session Destroyed
```

---

# Important Commands

Create Superuser

```bash
python manage.py createsuperuser
```

Run Server

```bash
python manage.py runserver
```

Open Shell

```bash
python manage.py shell
```

---

# Frequently Asked Interview/Exam Questions

### Short Questions

1. What is a Cookie?
2. What is a Session?
3. Differentiate between Cookies and Sessions.
4. How do you create a cookie in Django?
5. How do you delete a cookie?
6. How do you create a session?
7. How do you delete a session?
8. What is Authentication?
9. Explain `authenticate()`.
10. Explain `login()`.
11. Explain `logout()`.
12. What is `request.user.is_authenticated`?
13. What is the purpose of `login_required`?
14. How do you create a user in Django?
15. Why are sessions preferred over cookies for authentication?

---

# Unit VI Summary

- Cookies store small pieces of data in the user's browser, while sessions store data securely on the server.
- Cookies are suitable for remembering user preferences, whereas sessions are mainly used for authentication and maintaining login state.
- Django provides methods to create, read, update, and delete cookies and sessions.
- Django's authentication system verifies user identity using `authenticate()`.
- The `login()` function creates a user session, while `logout()` ends it.
- Protected views can be secured using `request.user.is_authenticated` or the `@login_required` decorator.
- Django automatically hashes passwords and provides a secure authentication framework for web applications.