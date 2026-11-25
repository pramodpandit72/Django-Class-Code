Practice questions:
Q1. 

A college wants to collect student feedback. Create a Feedback model with feedback_id (unique), student_name, subject and comments. Create a ModelForm to accept feedback and validate that comments contain at least 10 characters. Save valid feedback, display all feedback records ordered by student_name, show the total number of records using count(), and provide a view to update comments.

Q2. 

A shop maintains product details. Create a Product model with product_code (unique), product_name, category, price and quantity. Insert at least four records using Django ORM. Display products ordered by product_name, show the total number of products using count(), calculate the average price using Avg, and provide a view to update the price of a selected product.

Q3. 

A company maintains department and employee records. Create Department and Employee models with a ForeignKey relationship. Include department_name and employee_id (unique). Insert at least two departments and four employees using ORM. Display employee names along with their department names, ordered by employee name. Show the total number of employees using count() and provide a view to update an employee's department.

Q4. 

Create a Django application that counts how many times a visitor visits a webpage. Store the visit count in a cookie and increment it whenever the visitor opens the page. Display the updated count in an HTML template. Also provide a button to reset the visit count to zero.

Q5. 

Create a Django application that accepts a student's name and roll number through an HTML form. Store these details in a Django session and display them on another webpage. Provide a button to clear the session data and display a message after clearing it.