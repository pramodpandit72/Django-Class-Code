from django.http import HttpResponse, HttpResponseServerError

def handler404(request, exception):
    return HttpResponse("<body style='background-color: black; color:red'> <h1>Dear user, the page you are looking for does not exist<h1> </body>", status=404)

# def handler500(request):
#     return HttpResponse("<body style='background-color: black; color:red'> <h1>Oops! there seems to be a server error <h1> </body>", status=500)

def handler500(request):
    return HttpResponseServerError("<body style='background-color: black; color:red'> <h1>Oops! there seems to be a server error <h1> </body>")