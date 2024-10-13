from django.shortcuts import render
from django.http import HttpResponse
from .models import Marks

globalList=[]

# Create your views here.
def index(req):
    return render(req,"index.html")
def show(req):
    return render(req,"show.html")

def storeData(req):
    m1=int(req.POST.get('M1'))
    m2=int(req.POST.get('M2'))
    m3=int(req.POST.get('M3'))
    name=req.POST.get('name')
    total=m1+m2+m3
    
    Marks.objects.create(
        m1=m1,
        m2=m2,
        m3=m3,
        name=name,
        total=total
    ).save()
    globalList=Marks.objects.all()
    return render(req,"show.html",{"data":globalList})


def serach(req):
    
    total=req.POST.get('total')
    globalList=Marks.objects.filter(total=total)
    return render(req,"show.html",{"data":globalList})


def delete(req,name):
    data=Marks.objects.get(name=name)
    data.delete()
    globalList=Marks.objects.all()
    return render(req,"show.html",{"data":globalList})