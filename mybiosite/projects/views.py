from django.shortcuts import render
from projects.models import Project


# Create your views here.

def project_index(request):
    projects = Project.objects.filter(is_published=True)
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_technology(request, technology):
    projects = Project.objects.filter(
        technologies_used__name__contains=technology
    )
    context = {
        "technology": technology,
        "projects": projects
    }
    return render(request, "project_technology.html", context)


def project_detail(request, sub_url):
    project = Project.objects.get(sub_url=sub_url)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
