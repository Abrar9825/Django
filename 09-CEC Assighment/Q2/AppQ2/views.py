from django.shortcuts import render, redirect

car_list = []

def home(request):
    return render(request, 'home.html')

def add_car(request):
    if request.method == 'POST':
        model = request.POST.get('model')
        price = request.POST.get('price')
        car_dict ={
        'model': model,
        'price' : price
        }
        car_list.append(car_dict)
        return redirect('/delete_car/')
    return render(request, 'add_car.html')

def delete_car(request, model=None):
    for singleCar in car_list:
        if(singleCar["model"]==model):
            car_list.remove(singleCar)
    dictTemp={"cars":car_list}
    return render(request, 'delete_car.html', dictTemp)

