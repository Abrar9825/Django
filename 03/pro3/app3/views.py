from django.shortcuts import render, HttpResponse

# Create your views here.

def countVowel(e):
    vowel = 'aeiouAEIOU'
    num_vowel = 0
    for char in e:
        if char in vowel:
            num_vowel += 1
    return num_vowel

def index(req):
    return render(req,'index.html')

def loginpage(req):
    
    fname = req.GET.get('fname')
    lname = req.GET.get('lname')
    prime = req.GET.get('prime')

    if not prime:
        return HttpResponse("Please provide a prime number.")

    primeNumber = int(prime)

    flag = 1
    for i in range(2, primeNumber):
        if primeNumber % i == 0:
            flag = 0
            break

    fvowels = countVowel(fname)
    lvowels = countVowel(lname)

    if len(fname) > 4 and len(lname) > 4:
        if fvowels == 2 and lvowels == 2:
            if flag:
                return render(req, "home.html")
            else:
                return HttpResponse("Enter a Prime Number")
        else:
            return HttpResponse("First name and last name must have 2 vowels")
    else:
        return HttpResponse("First name and last name must have more than 4 characters")

def home(req):
    return render(req, "home.html")
