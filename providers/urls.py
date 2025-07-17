from django.urls import path
from . import views


urlpatterns = [\
    path('', views.mainhome, name='mainhome'),
    path('provider/', views.provhome, name='provhome'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('searchhome/', views.searchhome, name='searchhome'),
    
]