from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Users, Services

# Create your views here.
def provhome(request):
    return render(request, 'provhome.html')

def mainhome(request):
    return render(request, 'main.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Users.objects.filter(email=email, password=password).exists():
            user = Users.objects.get(email=email, password=password)
            if user.role == 'PROVIDER':
                return redirect('provhome')
            elif user.role == 'SEARCHER':
                return redirect('searchhome')
            else:
                messages.error(request, 'Invalid role')
        else:
            messages.error(request, 'Invalid credentials!!!')
    return render(request, 'login.html')

def searchhome(request):
    services = Services.objects.all()
    return render(request, 'searchhome.html', {'services': services})

def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('query')
        services = Services.objects.filter(title__icontains=search_query)
        return render(request, 'searchhome.html', {'services': services})
    return redirect('searchhome')

def register_view(request):
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile_picture')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        identity_number = request.POST.get('identity_number')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        role = request.POST.get('role', '').upper()
        if password == re_password:
            if Users.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            elif Users.objects.filter(identity_number=identity_number).exists():
                messages.error(request, 'Identity number already exists')
            elif role not in ['PROVIDER', 'SEARCHER']:
                messages.error(request, 'Invalid role selected')
            else:
                user = Users.objects.create(
                    profile_picture=profile_picture,
                    name=name,
                    surname=surname,
                    identity_number=identity_number,
                    phone_number=phone_number,
                    email=email,
                    password=password,
                    role=role
                )
                user.save()
                messages.success(request, f'{role.capitalize()} registered successfully')
                if role == 'PROVIDER':
                    return redirect('provhome')
                else:
                    return redirect('searchhome')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'register.html')