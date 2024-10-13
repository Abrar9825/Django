from django.shortcuts import render


books=[]
def index(req):
    return render(req,"index.html")

def addBook(req):
    return render(req,'addBook.html')
    

def bookPrice(req):
    return render(req,"bookPrice.html")



def addBooks(req):
    title=req.POST.get('title')
    author=req.POST.get('author')
    price=req.POST.get('price')
    books.append({
        'title':title,
        'author':author,
        'price':price,
        })
    return render(req, 'addBook.html')

def bookPriceFilter(req):
    max_price=req.POST.get('price')
    filterdBooks=[book for book in books if book['price'] < max_price]
    return render(req,'bookPrice.html',{'books':filterdBooks})

