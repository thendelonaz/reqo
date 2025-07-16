from django.shortcuts import render

# Create your views here.
def provhome(request):
    return render(request, 'provhome.html')

def mainhome(request):
    return render(request, 'main.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')