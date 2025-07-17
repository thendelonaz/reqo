from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def provhome(request):
    return render(request, 'provhome.html')

def mainhome(request):
    return render(request, 'main.html')

def login_view(request):
    return render(request, 'login.html')

def searchhome(request):
    return render(request, 'searchhome.html')

def register_view(request):
    if request.method == 'POST':
        # Handle registration logic here
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        role = request.POST.get('role', '').upper()
        # Add your registration logic here, such as saving to the database
        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            elif role not in ['PROVIDER', 'SEARCHER']:
                messages.error(request, 'Invalid role selected')
            elif role == 'PROVIDER':
                user = User.objects.create_user(username=email, first_name=name, last_name=surname, email=email, password=password)
                user.save()
                user_login = auth.authenticate(username=email, password=password)
                auth.login(request, user_login)
                return redirect('provhome')
            elif role == 'SEARCHER':
                user = User.objects.create_user(username=email, first_name=name, last_name=surname, email=email, password=password)
                user.save()
                user_login = auth.authenticate(username=email, password=password)
                auth.login(request, user_login)
                messages.success(request, 'Searcher registered successfully')
                return redirect('searchhome')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'register.html')