from django.shortcuts import render
from projects.models import Project, Technology


def get_project_technologies():
    technologies = Technology.objects.all().order_by('-name')
    return technologies

def get_base_context():
    return {
        'project_technologies': get_project_technologies(),
    }

# Create your views here.

def project_index(request):
    projects = Project.objects.filter(is_published=True)
    context = get_base_context()
    context['projects'] = projects
    return render(request, 'project_index.html', context)


def project_technology(request, technology):
    projects = Project.objects.filter(
        technologies_used__name__contains=technology
    )
    context = get_base_context()
    context['projects'] = projects
    context['technology'] = technology
    return render(request, 'project_technology.html', context)


def project_detail(request, sub_url):
    project = Project.objects.get(sub_url=sub_url)
    context = get_base_context()
    context['project'] = project
    return render(request, 'project_detail.html', context)
