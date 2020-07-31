from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "core/home.html")

def productos(request):
    return render(request, "core/productos.html")

def cartas(request):
    return render(request, "core/cartas.html")
