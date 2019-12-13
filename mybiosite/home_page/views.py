from django.shortcuts import render
from projects.models import Project

# Create your views here.

def home_page(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'home_page.html', context)

def my_page(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'mypage.html', context)