from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("<body style='background-color: black; color:red'> <h1>Dear user, the page you are looking for does not exist<h1> </body>", status=404)