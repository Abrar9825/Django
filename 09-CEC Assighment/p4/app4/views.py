from django.shortcuts import render
ls=[]
def home(req):
	return render (req,'home.html')

def addstudent(req):
	return render(req,'addstudent.html')

def adddata(req):
	student_no=req.GET.get('student_no')
	student_name=req.GET.get('student_name')
	theory1=int(req.GET.get('theory1'))
	theory2=int(req.GET.get('theory2'))
	theory3=int(req.GET.get('theory3'))
	practical1=int(req.GET.get('practical1'))
	practical2=int(req.GET.get('practical2'))
	totalmark=theory1+theory2+theory3+practical1+practical2
	passingmark= 40 * 5
	result = 'pass' if totalmark >= passingmark else 'fail'
	


	dict1={'student_no':student_no,'student_name':student_name,'theory1':theory1,'theory2':theory2,'theory3':theory3,'practical1':practical1,'practical2':practical2,'result':result}
	ls.append(dict1)
	dict2={'students':ls}
	
	return render(req,'show.html',dict2)





