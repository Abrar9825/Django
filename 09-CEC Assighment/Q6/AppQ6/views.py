from django.shortcuts import render, redirect

user_details = []

def home(request):
    return render(request, 'home.html', {'users': user_details})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_data = {
            'username': username,
            'email': email,
            'password': password,
        }
        user_details.append(user_data)
        return redirect('login') 
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        for user in user_details:
            if user['username'] == username and user['password'] == password:
                return redirect('home') 
    return render(request, 'login.html')
