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

    return render(request, 'menu.html', {'menu': newmenu})