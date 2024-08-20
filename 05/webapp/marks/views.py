from django.shortcuts import render,HttpResponse
MarkSave = []
count = 0

def index(request):
    return render(request, "index.html")

def SaveMarks(request):
    EnNo = request.GET.get("EnNo")
    Uname = request.GET.get("Uname")
    Subject1 = int(request.GET.get("Subject1"))
    Subject2 = int(request.GET.get("Subject2"))

    total_marks = Subject1 + Subject2
   
    MarkSave.append({
        "ENROLLMENT": EnNo,
        "USERNAME": Uname,
        "Subject_1": Subject1,
        "Subject_2": Subject2,
        "Total_Marks" : total_marks
    })    
    

    total_students = len(MarkSave) 
    return render(request, "ShowData.html", {"total_students": total_students})

def ShowData(request):
    return render(request, "ShowData.html")


def Result(request):
    EnNo = request.GET.get("EnNo")

    student_data = 0
    for result in MarkSave:
        if result["ENROLLMENT"] == EnNo:
            student_data = result
        else:
            print("Not found")
    
    if student_data:
        return render(request, "result.html", {"student_data": student_data})
    else:
        return HttpResponse("Student not found")