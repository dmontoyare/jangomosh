from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # la funcion render acepta un tercer parametro el cual es un diccionario donde podemos enviar variables necesarias 
    return render(request, 'hello.html', {
        'name': 'Daniel'
    })
