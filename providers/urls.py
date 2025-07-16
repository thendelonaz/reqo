from django.urls import path
from . import views


urlpatterns = [\
    path('', views.mainhome, name='mainhome'),
    path('/provider', views.provhome, name='provhome'),
]