step1 :- create a class for model using which the table will be created
step2 :- create a migration file (python manage.py makemigrations)
step3 :- migrate the migration file (python manage.py migrate)

after all this , table will be created we will use sqlite (install extension SQLite viewr in vs code)









python manage.py shell

>>> from myapp.models import Emp
>>> Emp.objects.create(firstname='ashutosh', lastname='kumar',salary=56000,age=34)



python manage.py shell 

from myapp.models import Emp
Emp.objects.create(firstname='Ayush', lastname='kumar',salary='56000',age=34)
Emp.objects.create(firstname='Ritika', lastname='sharma',salary='76000',age=44)
Emp.objects.all()

exit()
<!-- <QuerySet [<Emp: Emp object (1)>, <Emp: Emp object (2)>]> -->


from myapp.models import Emp

// to edit
e = Emp.objects.get(pk=2)
e.salary = 54000
e.save()

// to Delete
e = Emp.objects.get(pk=1)
e.delete()
