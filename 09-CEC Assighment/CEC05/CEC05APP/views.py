from django.shortcuts import render

bikes = []  # List to store bike data

def index(req):
    return render(req, "index.html")

def addBike(req):
    return render(req, 'addBike.html')

def showData(req):
    return render(req, "showData.html")  

def addBikes(req):
    if req.method == "POST":
        name = req.POST.get('name')
        color = req.POST.get('color')
        price = req.POST.get('price')
        bikes.append({
            'name': name,
            'color': color,
            'price': price,
        })
    return render(req,"showData.html",{"bikesData": bikes}) 

def deleteData(req,name):
    for bike in bikes:
        if(bike['name']==name):
            bikes.remove(bike)
            
    return render(req,"showData.html",{"bikesData": bikes})