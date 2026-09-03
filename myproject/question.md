1. Create a view that accepts two variables as name and program. Assign the values and display the details as an   HttpResponse in blue color on th browser by creating a path in urls.py

2. Create a view(function) that creates 5 variables as course1, course2, course3, course4, course5. Assign the marks to these variables as interger values, then calculate the percentage of the student and the pront the result as an HttpResponse on the browser by creating a path as "marks/" in urls.py. 

3. Create a view that accepts a variable a marks and assign value to it. Print the grades as an HttpResponse.Use the following conditions:

marks > 80 && marks <= 100, Print Grade A in dark green color
marks > 60 && marks <= 80, Print Grade B in dark blue color
marks > 40 && marks <= 60, Print Grade C in dark blue color
marks < 40, print fail in red color

4. Create a view that accepts a list of following food items
Pizza
Burger
Noodles
Momos
print these items on the browser

DISM /Online /Cleanup-Image /RestoreHealth



# Create a Path 'menu/'. Use regex to pass two parameters category and subcategory. Subcategory is an optional parameter. Both can acccept digits and alphabets and space

Case1: If you specify subcategory in URL
localhost:8000/menu/chinese/noodles 

You have choosen category: chinese
You have choosen subcategory: noodles

Case2: If you donot specify subcategory in URL
localhost:8000/menu/chinese/noodles 

You have choosen category: chinese
You have choosen subcategory: not specified


# Create a function that creates a list of dictionaries having food items with keys as "name" and "price".
 newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]

Render the intems as an html table in the template using DTL. Also, The background color of the free items should pink


# Create a function that creates a list of dictionaries having food items with keys as "name" and "price".
 newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]

The user must be able to pass the URL parameter as item_name and fetch the information os the specified item name

