from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, "login.html")

def login(req):
    username = req.GET.get("username")
    password = req.GET.get("password")

    if username == 'abrar' and password == '123':
        return render(req, "login.html") 
    else:
        return HttpResponse("Login failed. Please check your credentials.") 
