from django.shortcuts import render
ls=[]
def home(req):
	return render(req,'home.html')
# Create your views here.

def collegedetail(req):
	return render(req,'college.html')

def Adddetail(req):
	collegename=req.GET.get('collegename')
	collegecity=req.GET.get('collegecity')

	dict1={'collegename':collegename,'collegecity':collegecity}
	ls.append(dict1)
	dict2={'colleges':ls}
	return render (req,'show.html',dict2)

def search(req):
	return render(req,'search.html')

def searching(req):
	
	city= req.GET.get('collegecitys')
	templs=[]
	for citys in ls:
		if(citys['collegecity']==city):
			templs.append(citys)

	dict3={'colleges':templs}
	return render(req,'shows.html',dict3)

