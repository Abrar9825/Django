from django.shortcuts import render
from .models import Register
from django.http import HttpResponse
allList=[]
def index(req):
    return render(req, "index.html")
def show(req):
    return render(req, "show.html")
def login(req):
    return render(req, "login.html")

def storedata(req):
    name = req.POST.get("username")
    email = req.POST.get("email")
    password = req.POST.get("password")
    choice = req.POST.get("firstchoice")
    gender = req.POST.get("gender")
    interests = req.POST.getlist("interests")

    Register.objects.create(
        name=name,
        email=email,
        password=password,  
        choice=choice,
        gender=gender,
        interests=interests,
    )

    return render(req, "login.html")



def logincheck(req):
    name = req.POST.get("name")
    password = req.POST.get("password")

    db_user = Register.objects.filter(name=name).first()

    if db_user.password == password: 
        print("Password is correct")
        allList=Register.objects.all()
        return render(req, "show.html",{"data":allList})
    else:
        print("Password is incorrect")
        return HttpResponse("Password is incorrect.")
    
    
    
def removeData(req,name):
    data=Register.objects.get(name=name)
    data.delete()
    allList=Register.objects.all()
    return render(req,"show.html",{"data":allList})