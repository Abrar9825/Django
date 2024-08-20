from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def surveyForm(req):
	return render(req,"survey.html")

def red(req):
	return render(req,"red.html")

def green(req):
	return render(req,"green.html")

#function to check string contain vowel or not
def details(name):
	vowels=['a','e','i','o','u','A','E','I','O','U']
	vowelCounter=0
	validationCounter=0

	if len(name)>=10:
		#loop for find vowels from string
		for i in name:
			if i in vowels:
				vowelCounter=vowelCounter+1

	#verify string contains two vowel or not
	if vowelCounter==2:
		validationCounter=validationCounter+1

	return validationCounter

#function to check number is prime or not
def checkPrime(num):
	flag=0
	validationCounter=0
	for i in range(1,int(num)+1):
		if(int(num)%i==0):
			flag=flag+1

	if flag==2:
		validationCounter=validationCounter+1

	return validationCounter

#handle request of verifyDetails
def verifyDetails(req):
	firstname=req.GET.get("firstname")
	lastname=req.GET.get("lastname")
	age=req.GET.get("age")
	#validation counter
	validationCounter=0
	
	verifyFN=details(firstname)
	verifyLN=details(lastname)
	verifyAge=checkPrime(age)

	validationCounter=verifyFN+verifyLN+verifyAge
	if int(validationCounter)==3:
		return render(req,"green.html")
	
	return render(req,"red.html")