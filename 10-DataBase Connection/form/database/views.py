from django.shortcuts import render
from .models import Student
# Create your views here.
globalList=[]
def index(req):
    return render(req,"index.html")

def savedata(req):
    no=req.GET.get('no')
    name=req.GET.get('name')
    gender=req.GET.get('gender')
    hobbies=req.GET.getlist('hobbies')
    course=req.GET.get('course')
   
    hobbies_str=" ".join(hobbies)
   
    name=req.GET.get('name')
    Student.objects.create(
        no=no,
        name=name,
        gender=gender,
        hobbies=hobbies_str,
        course=course,
        ).save()
    
    print(globalList)
    return render(req,"index.html")

def showdata(req):
    globalList=Student.objects.all()
    return render(req,"showdata.html",{"dataDict":globalList})
