from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
#

def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse(now)

# 
def hello(request):
    return HttpResponse("Hello World");

def home(request):
    return HttpResponse("""<h1 style='color:red'> 
    Welcome to Home Page</h1>""");

def menuitem(request):
    item = "cake"
    return HttpResponse("The name of the item is "+item);
    # return HttpResponse(f"The name of the item is {item}")

def menuitems(request):
    items={
        'pizza':'Pizza coast Rs. 500',
        'burger':'Burger costs Rs. 25',
        'noodles':'Noodles cost Rs. 40'
    }
    content = '<h1>Menu items </h1>'
    for item, description in items.items():
        content+=f'<li>{item}:{description}</li>'
    return HttpResponse(content)
    
def greet(request, name):
    return HttpResponse(f"Hello {name}! Welcome to our website")

def menuitems1(request, dish) :
    items={
        'pizza':'Pizza coast Rs. 500',
        'burger':'Burger costs Rs. 25',
        'noodles':'Noodles cost Rs. 40'
    }
    discription = items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + discription)

def menuitems2(request, dish) :
    items={
        'pizza':'Pizza coast Rs. 500',
        'burger':'Burger costs Rs. 25',
        'noodles':'Noodles cost Rs. 40'
    }
    if dish in items:
        discription = items[dish]
        return HttpResponse(f"<h2>{dish}</h2>" + discription)
    else:
        return HttpResponse(f"<h2>{dish}</h2>" + "Not found in the menu")
    
# Dynamic URL
def recipe(request): # recipe/?food=cake
    food = request.GET.get('food')
    if not food:
        return HttpResponse('Food parameter is missing', status=404)    
    return HttpResponse(f'Recipe is available for {food}')

def addition(request): # /addition/?value1=&value2=4
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')
    result = int(value1) + int(value2)
    return HttpResponse(f'Result of addition is {result}')

def calculate(request):
    operation = request.GET.get('operation')
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')

    # if operation == "+":
    #     result = int(value1) + int(value2) # %2B = +
    # elif operation == "-":
    #     result = int(value1) - int(value2)
    # elif operation == "*":
    #     result = int(value1) * int(value2)
    # elif operation == "/":
    #     result = int(value1) / int(value2)
    # else:
    #     result = "Invalid"

    # return HttpResponse(result)

    try:
        value1 = float(value1)
        value2 = float(value2)
    except ValueError:
        return HttpResponse("Invalid Operation")
    if operation == "add":
        result = value1 + value2
    elif operation == "subtract":
        result = value1 - value2
    elif operation == "multiply":
        result = value1 * value2
    elif operation == "divide":
        result = value1 / value2
    else:
        return HttpResponse("Invalid Operation")
    return HttpResponse(result)

# Regular Expressions
def user_profile(request, username):
    return HttpResponse(f'User profile: {username}')

def item_detail(request, item_id):
    return HttpResponse(f'Item ID: {item_id}')

def restro_detail(request, category, subcategory):
    # if(subcategory == ''):
    if not subcategory:
        return HttpResponse(f'Category: {category} and Subcategory: Not provided')
    return HttpResponse(f'Category: {category} and Subcategory: {subcategory}')

# Templates
def home1(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Dynamic templates
def menu(request):
    menuitem={'name':'Noodles'}
    return render(request, 'menu.html', menuitem)

def menu1(request):
    newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]

    return render(request, 'menu1.html', {'mains': newmenu})

# Template Inheritance
def home2(request):
    return render(request, 'home.html')

def about2(request):
    return render(request, 'about.html')

def menuitems2(request):
    return render(request, 'menuitems.html')







# ------------------ Class Code -----------------------
def details(request):
    name = "Ankit"
    program = "CSE"
    # return HttpResponse("<h2 style='color:blue'>The name of the Student " + name + ". " + " He belongs to " + program + "</h2>");
    return HttpResponse(f"<h2 style='color:blue'>The name of the Student {name}. He belongs to {program} </h2>");

def newdetails(request):
    # return HttpResponse("<h1>This is a Heading</h1>" \
    #                     "<p>This is a paragraph</p>")
    return HttpResponse("""<h1>This is a Heading</h1>
                        <p>This is a paragraph</p>""")

def percent(request):
    course1 = 50
    course2 = 60
    course3 = 70
    course4 = 80 
    course5 = 90
    result = (float(course1 + course2 + course3 + course4 + course5)/500) * 100
    return HttpResponse(f'<h2 style="color:green; border:2px solid blue">Percentage {result} </h2>')

def multiple(request):
    number = 5
    result = ""
    for i in range(1, 11):
        result += f'{number} x {i} = {number * i} <br>'
    return HttpResponse(result)

def grade(request):
    marks = 45

    if marks > 80 and marks <= 100:
        result = "<h1 style=color:green>Grade A </h1>"
    elif marks > 60 and marks <= 80:
        result = "<h1 style=color:blue>Grade B </h1>"
    elif marks > 40 and marks <= 60:
        result = "<h1 style=color:orange>Grade C </h1>"
    else:
        result = "<h1 style=color:red>Fail </h1>"

    return HttpResponse(result)

def food(request):
    fooditems = ["Pizza", "Burger", "Noodles", "Momos"]
    itemcontent = "<h2>The food items available are: </h2>"
    for item in fooditems:
        itemcontent += f"<p>{item}</p>"
    return HttpResponse(itemcontent)

def food1(request):
    fooddetails = {
        "name": "Pizza",
        "Price": 200,
        "Size": "Regular"
    }
    content = "<h1>Food List: </h1>"
    for key, value in fooddetails.items():
        content += f'{key} {value} <br>'
    return HttpResponse(content)

def studentdetails(request):
    studentinfo = [
        ["Ayush", 67],
        ["Manish", 50],
        ["Ankit", 60]
    ]

    content = """
    <table border = 1>
    <tr>
    <th>Name</th>
    <th>Marks</th>
    </tr>
    """
    for i in studentinfo:
        content += f"""
        <tr>
        <td>{i[0]}</td>
        <td>{i[1]}</td>
        </tr>
        """
    content += "</table>"
    return HttpResponse(content)

def studentdetails1(request):
    studentinfo = [
        {"Name": "Amit", "Marks": 90, "Course": "Django"},
        {"Name": "Manish", "Marks": 86, "Course": "React"},
        {"Name": "Ritik", "Marks": 76, "Course": "Node"},
        {"Name": "Ankit", "Marks": 96, "Course": "Next.js"},
    ]

    # content = """
    # <table border = 1>
    # <tr>
    # <th>Name</th>
    # <th>Marks</th>
    # <th>Course</th>
    # </tr>
    # """
    # for i in studentinfo:
    #     content += f"""
    #     <tr>
    #         <td>{i["Name"]}</td>
    #         <td>{i["Marks"]}</td>
    #         <td>{i["Course"]}</td>
    #     </tr>
    #     """
    # content += "</table>"
    

    # content = "Student list: <br>"
    # for student in studentinfo:
    #     for key, value in student.items():
    #         content += f"{key} {value} <br>"
    #     content += "<br>"


    content = "<table border = 1>"
    for colnames in studentinfo[0].keys():
        content += f"""
        <th>{colnames}</th>
        """

    for i in studentinfo:
        content += "<tr>"
        for key, value in i.items():
            content += f"""
            <td>{value}</td>
            """
    content += "</tr> </table>"

    return HttpResponse(content)

def studentdetails2(request):
    studentinfo = {
        "Amit": {"Marks": 90, "Course": "Django"},
        "Manish": { "Marks": 86, "Course": "React"},
        "Ritik": {"Marks": 76, "Course": "Node"},
    }

    # content = ""
    # for name, details in studentinfo.items():
    #     content += f"Name: {name}<br>"
    #     content += f"Marks: {details['Marks']}<br>"
    #     content += f"Course: {details['Course']}<br><br>"

    content = """
    <table border = 1 >
    <tr>
    <th>Name</th>
    <th>Marks</th>
    <th>Course</th>
    </tr>
    """
    for key, value in studentinfo.items():
        content += f"""
        <tr>
        <td>{key}</td>
        <td>{value['Marks']}</td>
        <td>{value['Course']}</td>
        </tr>
        """
    content += "</table>"
    return HttpResponse(content)

# ------------------------- Dynamic URL --------------
def greetings(request, name):
    return HttpResponse(f"Welcome, {name}")

def add(request, num1, num2):
    return HttpResponse(f'The result is {num1 + num2}')

def foodie(request, foodvalue):
    # fooditems = ["noodeles", "pizza", "Icecream, Bread"]
    fooditems = {
        "Pizza": "size is regular, price is 50",
        "Burger": "size is medium, price is 100",
        "icecream": "Icecream is large, price is 40"
    }
    if foodvalue not in fooditems:
        return HttpResponse(f"The selected item {foodvalue} is not available")
    # return HttpResponse(fooditems[foodvalue])
    return HttpResponse(f"You have selected {foodvalue}. <h4 style=color:violet> {fooditems[foodvalue]} </h4>")

def calculation(request):
    operation = request.GET.get('operation')
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')

    # try:
    #     value1 = int(value1)
    #     value2 = int(value2)
    # except:
    #     return HttpResponse("Enter valid number")
    # result = None

    if operation == "add":
        result = int(value1) + int(value2)
    elif operation == "subtract":
        result = int(value1) - int(value2)
    elif operation == "multiply":
        result = int(value1) * int(value2)
    elif operation == "divide":
        result = int(value1) / int(value2)
    else:
        result = "Invalid"

    return HttpResponse(f"The result of {operation} is {result}")

# --------------- Regular Exprression ---------------
def customer_profile(request, customername):
    return HttpResponse(f'Customer Profile: {customername}')

def user_profile(request, username):
    return HttpResponse(f'User Profile: {username}')

def item_detail2(request, item):
    return HttpResponse(f'Item Id: {item}')

def archive_details(request, year, month):
    return HttpResponse(f'Archive Year: {year}, Month: {month}')


def food_category(request, category, subcategory):
    # if(subcategory == ''):
    if not subcategory:
        return HttpResponse(f'You have choosen category: {category} and You have choosen subcategory: not specified')
    return HttpResponse(f'You have choosen category: {category} and  You have choosen subcategory: {subcategory}')


# ---------------------- Error Handling ---------------------------------
# Simulate Error 500 (server error)
def dividebyzero(request):
    a = 10
    result = a/0
    return HttpResponse(result)


# ----------------- Templates ----------------------

def mytemplate(request):
    data={'name': "Ankit"}
    return render(request, 'test.html', data)

def fooddata(request):
    newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]

    return render(request, 'menu2.html', {'menu': newmenu})

def fooddata1(request, item_name):
    newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]
    return render(request, 'menu3.html', {'menu': newmenu, 'item_name': item_name})

def testimage(request):
    return render(request, 'testimage.html')

def productlist(request):
    products=[
        {'name':'smartphone', 'brand':'Samsung', 'price': 45000, 'image': 'images.jpeg'},
        {'name':'laptop', 'brand':'Dell', 'price': 100000, 'image': 'images1.jpeg'},
        {'name':'headphone', 'brand':'Boat', 'price': 50000, 'image': 'images2.jpeg'}
    ]

    return render(request, 'products.html', {'product_list': products})

def shopingList(request):
    products=[
        {'name':'smartphone', 'brand':'Samsung', 'price': 45000, 'image': 'images.jpeg'},
        {'name':'laptop', 'brand':'Dell', 'price': 100000, 'image': 'images1.jpeg'},
        {'name':'headphone', 'brand':'Boat', 'price': 50000, 'image': 'images2.jpeg'}
    ]

    return render(request, 'shoping.html', {'product_list': products})

def shopingDetail(request, shopingItem):
    products=[
        {'name':'smartphone', 'brand':'Samsung', 'price': 45000, 'image': 'images.jpeg'},
        {'name':'laptop', 'brand':'Dell', 'price': 100000, 'image': 'images1.jpeg'},
        {'name':'headphone', 'brand':'Boat', 'price': 50000, 'image': 'images2.jpeg'}
    ]

    return render(request, 'shopingDetail.html', {'product_list': products, 'shoping_item':shopingItem})


def greeting(request, name, time_of_day):
    # http://127.0.0.1:8000/greet/Rahul/evening/
    if time_of_day == "morning":
        message = f"Good Morning, {name}!"

    elif time_of_day == "afternoon":
        message = f"Good Afternoon, {name}!"

    elif time_of_day == "evening":
        message = f"Good Evening, {name}!"

    else:
        message = "Invalid Time of Day"

    return render(request, "greeting.html", {"greeting": message})




def departments(request):
    department_list = [
        "Computer Science",
        "Information Technology",
        "Mechanical Engineering",
        "Civil Engineering",
        "Electrical Engineering"
    ]

    return render(request, "departments.html", {
        "departments": department_list
    })


def department_detail(request, department_name):
    department_list = [
        "Computer Science",
        "Information Technology",
        "Mechanical Engineering",
        "Civil Engineering",
        "Electrical Engineering"
    ]

    if department_name in department_list:
        message = f"You selected: {department_name}"
    else:
        message = "Department Not Available"

    return render(request, "department_detail.html", {
        "message": message
    })



# Template Inheritance 

def home4(request):
    return render(request, 'home4.html')
def about4(request):
    return render(request, 'about4.html')
def food4(request):
    newmenu=[
            {'name':'Noodles', 'price':40, 'size':'medium', 'image': 'images.jpeg'},
            {'name':'Pizza', 'price':100, 'size':'small', 'image': 'images1.jpeg'},
            {'name':'Bread', 'price':'free', 'size':'large', 'image': 'images2.jpeg'},
        ]
    return render(request, 'food4.html', {'menu': newmenu})

def testcss(request):
    return render(request, 'testcss.html')

def items(request):
    products=[
        {'name': 'laptop'},
        {'name': 'smartphone'},
        {'name': 'headphones'},
    ]
    return render(request, 'items.html', {'products': products})

def itemdetails(request, name):
    products={
        'laptop':{'brand':'Dell', 'price':20000},
        'smartphone':{'brand':'smasung', 'price':50000},
        'headphone':{'brand':'Boat', 'price':70000},
    }
    item = products.get(name)
    if item:
        return render(request, 'itemdetails.html', {'name':name, 'brand':item['brand'], 'price':item['price']})




#  ----------- CA --------------


def canteen(request):
    Food = [
        {'item_id': '101', 'name': 'Bread', 'category': 'Breakfast', 'price': 10, 'available': 'Yes'},
        {'item_id': '102', 'name': 'Poha', 'category': 'Breakfast', 'price': 30, 'available': 'Yes'},
        {'item_id': '103', 'name': 'Samosa', 'category': 'Lunch', 'price': 15, 'available': 'No'},
        {'item_id': '104', 'name': 'Sandwich', 'category': 'Lunch', 'price': 50, 'available': 'Yes'},
        {'item_id': '105', 'name': 'Thali', 'category': 'Dinner', 'price': 100, 'available': 'No'},
        {'item_id': '106', 'name': 'Biryani', 'category': 'Dinner', 'price': 120, 'available': 'No'},
        {'item_id': '107', 'name': 'Coffee', 'category': 'Snacks', 'price': 25, 'available': 'Yes'},
        {'item_id': '108', 'name': 'Juice', 'category': 'Snacks', 'price': 40, 'available': 'No'},
    ]
    return render(request, 'canteen.html',{'Food':Food})

def category(request, category):
    Food = [
        {'item_id': '101', 'name': 'Bread', 'category': 'Breakfast', 'price': 10, 'available': 'Yes'},
        {'item_id': '102', 'name': 'Poha', 'category': 'Breakfast', 'price': 30, 'available': 'Yes'},
        {'item_id': '103', 'name': 'Samosa', 'category': 'Lunch', 'price': 15, 'available': 'No'},
        {'item_id': '104', 'name': 'Sandwich', 'category': 'Lunch', 'price': 50, 'available': 'Yes'},
        {'item_id': '105', 'name': 'Thali', 'category': 'Dinner', 'price': 100, 'available': 'No'},
        {'item_id': '106', 'name': 'Biryani', 'category': 'Dinner', 'price': 120, 'available': 'No'},
        {'item_id': '107', 'name': 'Coffee', 'category': 'Snacks', 'price': 25, 'available': 'Yes'},
        {'item_id': '108', 'name': 'Juice', 'category': 'Snacks', 'price': 40, 'available': 'No'},
    ]

    data = ""

    for item in Food:

        if item['category'] == category:

            data += f"""
            <h2>{item['name']}</h2>
            <p>Item ID: {item['item_id']}</p>
            <p>Category: {item['category']}</p>
            <p>Price: {item['price']}</p>
            <p>Availability: {item['available']}</p>
            <hr>
            """

    if data == "":
        return HttpResponse("No Items Available in This Category")

    return HttpResponse(data)

def item(request, item_id):
    Food = [
        {'item_id': '101', 'name': 'Bread', 'category': 'Breakfast', 'price': 10, 'available': 'Yes'},
        {'item_id': '102', 'name': 'Poha', 'category': 'Breakfast', 'price': 30, 'available': 'Yes'},
        {'item_id': '103', 'name': 'Samosa', 'category': 'Lunch', 'price': 15, 'available': 'No'},
        {'item_id': '104', 'name': 'Sandwich', 'category': 'Lunch', 'price': 50, 'available': 'Yes'},
        {'item_id': '105', 'name': 'Thali', 'category': 'Dinner', 'price': 100, 'available': 'No'},
        {'item_id': '106', 'name': 'Biryani', 'category': 'Dinner', 'price': 120, 'available': 'No'},
        {'item_id': '107', 'name': 'Coffee', 'category': 'Snacks', 'price': 25, 'available': 'Yes'},
        {'item_id': '108', 'name': 'Juice', 'category': 'Snacks', 'price': 40, 'available': 'No'},
    ]

    for food in Food:

        if food['item_id'] == item_id:

            data = f"""
            <h2>{food['name']}</h2>
            <p>Item ID: {food['item_id']}</p>
            <p>Category: {food['category']}</p>
            <p>Price: {food['price']}</p>
            <p>Availability: {food['available']}</p>
            """

            return HttpResponse(data)

    return HttpResponse("Item Not Found")


# --------------------------------------------------------------------------
# Testing in Dajango

def sampletest(request):
    return HttpResponse('This is a smaple test page')

def sampletest1(request, id):
    return HttpResponse(f'The is is {id}')

def new(request):
    return HttpResponse('Some content')

def old(request):
    return redirect('/new/')


# ---------- Forms in Django ---------------

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def simpleform(request):
    if request.method == 'GET':
        htmlform = """
        <form method="Post">
        <input type="text" name="textbox1"> <br>
        <input type="text" name="textbox2"> <br>
        <input type="submit">
        </form>
        """

        return  HttpResponse(htmlform)

    else:
        t1 = request.POST.get("textbox1")
        t2 = request.POST.get("textbox2")
        return HttpResponse(f"The values are {t1} and {t2}")


from django.middleware.csrf import get_token
def simpleform1(request):
    csrf_token = get_token(request)
    # print(csrf_token)
    if request.method == 'GET':
        htmlform = f"""
        <form method="Post">
        <input type="hidden" name="csrfmiddlewaretoken" value={csrf_token}>
        <input type="text" name="textbox1"> <br>
        <input type="text" name="textbox2"> <br>
        <input type="submit">
        </form>
        """

        return  HttpResponse(htmlform)

    else:
        t1 = request.POST.get("textbox1")
        t2 = request.POST.get("textbox2")
        return HttpResponse(f"The values are {t1} and {t2}")

def htmlform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name and email and password:
            return HttpResponse(f'Form submitted successfullly. The details are {name}, {email}, {password}')
        else:
            return HttpResponse(f'Fill all the Details')
    else:    
        return render(request, 'htmlform.html')



def validate(request):
    submitted_details = None
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        name_error = None
        email_error = None
        password_error = None

        if not name:
            name_error = "Name is required"
        if not email:
            email_error = "Email is required"
        if not password or len(password) < 6:
            password_error = "Password should be atleast 6 chars long"
        if name_error or email_error or password_error:
            return render(request, 'validate_form.html', {
                'name':name,
                'email':email,
                'password':password,
                'name_error':name_error,
                'email_error':email_error,
                'password_error':password_error
            })
        submitted_details = {'name':name, 'email':email, 'password':password}
    return render(request, 'validate_form.html', {'submitted_details':submitted_details})


from .forms import InputForm1
def from_submission(request):
    if request.method == 'POST':
        form = InputForm1(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully")

    form = InputForm1()
    
    return render(request, 'InputForm1.html',{'form': form})


from  .forms import InputForm2
def form_submission2(request):
    submitted_details = None
    if request.method == 'POST':
        form = InputForm2(request.POST, request.FILES)
        if form.is_valid():
            submitted_details = form.cleaned_data
    else:
        form = InputForm2()
    return render(request, 'InputForm2.html', {'form':form, 'submitted_details':submitted_details})

