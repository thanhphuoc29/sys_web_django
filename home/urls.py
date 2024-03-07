from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.Hello, name='hello'),
    path('home',views.Home,name='home')
]