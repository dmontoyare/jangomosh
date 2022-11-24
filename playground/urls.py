from django.urls import path
from  . import views

#Se define la variable especial urlpatterns, escribirla bien

urlpatterns = [
    path('hello/', views.say_hello)
]