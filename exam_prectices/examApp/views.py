from django.shortcuts import render
# from django.http import HttpResponse

gloablist=[]
# Create your views here.

def index(req):
     return render(req,"index.html")
def showData(req):
     return render(req,"showData.html")
def findUser(req):
     return render(req,"findUser.html")


def printLoginMethod(req):
    name=req.POST.get("name")
    m1=req.POST.get("m1")
    m2=req.POST.get("m2")
    localdict={
        "name":name,
        "m1":m1,
        "m2":m2
    }
    gloablist.append(localdict)
    print(gloablist)
    return render(req,"showData.html" ,{"dataOfStud":gloablist})

def find(req):
    user=req.POST.get("findname")
    templist=[item for item in gloablist if item['name']==user]
    return render(req,"showData.html" ,{"dataOfStud":templist})
   
def deleteData(req,name):
     # templist=[item for item in gloablist if item['name'] != name]
     templist=[]
     for item in gloablist:
          if item['name']==name:
               gloablist.remove(item)
     return render(req,"showData.html" ,{"dataOfStud":templist})


     
          