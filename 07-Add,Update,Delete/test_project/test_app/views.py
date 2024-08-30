from django.shortcuts import render
# from django.http import HttpResponse

globalList = []

def index(req):
    return render(req, 'index.html')

def showData(req):
    return render(req, 'showData.html')

def search(req):
    return render(req, 'search.html')

def studentSearch(req):
        templist=[]
        studentToSearch = req.POST.get('studentToSearch')
        print(f"Searching for: {studentToSearch}")
        for stud in globalList:
            if stud["name"] == studentToSearch:
                templist.append(stud)
        dict_temp = {"dataStored": templist}
        return render(req, "showData.html", dict_temp)


def SaveMarks(req):
  
        name = req.POST.get('name')
        enroll = req.POST.get('enroll')
        jmarks = req.POST.get('jmarks')
        pmarks = req.POST.get('pmarks')
        
        dictForStoreData = {
            "name": name,
            "enroll": enroll,
            "jmarks": jmarks,
            "pmarks": pmarks,
        }
        
        globalList.append(dictForStoreData)
        dict_temp = {"dataStored": globalList}
        return render(req, "showData.html", dict_temp)
    
    
def deleteData(req,name):
    for stud in globalList:
        if(stud['name']==name):
            globalList.remove(stud)
    dict_temp={"dataStored":globalList}
    return render(req,"showData.html",dict_temp)