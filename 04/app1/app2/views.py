from django.shortcuts import render
from django.http import HttpResponse

studentDatalist = []

def index(req):
    return render(req, "index.html")

def storeData(req):
    enroll = req.GET.get("number")
    username = req.GET.get("username")
    subject1 = req.GET.get("firstSubject")
    subject2 = req.GET.get("secondSubject")

    studentDataDict = {
        "enrollment": enroll,
        "username": username,
        "subject1": subject1,
        "subject2": subject2
    }

    studentDatalist.append(studentDataDict)
    userLength = len(studentDatalist)  # Corrected length function
    print(userLength)

    userLength = len(studentDatalist)  # Corrected length function
    return render(req,"countList.html",{'userLength': userLength})

def showData(req):
    return render(req, "showData.html", {'studentDatalist': studentDatalist})

def countList(req):
    return render(req, "countList.html")
