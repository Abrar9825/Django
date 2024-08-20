from django.shortcuts import render, HttpResponse

MarkSave = []

def index(request):
    return render(request, "index.html")

def SaveMarks(request):
    EnNo = request.POST.get("EnNo")
    Uname = request.POST.get("Uname")
    Subject1 = int(request.POST.get("Subject1"))
    Subject2 = int(request.POST.get("Subject2"))

    # Correct percentage calculation
    percentage = (Subject1 + Subject2) / 2
    
    MarkSave.append({
        "ENROLLMENT": EnNo,
        "USERNAME": Uname,
        "Subject_1": Subject1,
        "Subject_2": Subject2,
        "Percentage": percentage
    })    
    
    total_students = len(MarkSave)
    return render(request, "ShowData.html", {"total_students": total_students})

def ShowData(request):
    return render(request, "ShowData.html")

def Result(request):
    EnNo = float(request.GET.get("EnNo"))
    
    

    matching_students = []

    for student in MarkSave:
        if student['Percentage'] > EnNo:
            matching_students.append(student)
    
    if matching_students:
        return render(request, "result.html", {"students": matching_students,"usergive":EnNo})
    else:
        return HttpResponse("No students found with percentage greater than " + str(EnNo))
    