from django.shortcuts import render
from .models import Project

# Create your views here.
def figuras(request):
    projects = Project.objects.all()
    return render(request, "hero/figuras.html", {'projects':projects})
