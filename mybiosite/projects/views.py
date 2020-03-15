from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseNotFound, Http404
from projects.models import Project, Technology
from home_page.models import Link


def get_links():
    links = Link.objects.all().order_by('-name')
    return links


def get_project_technologies():
    technologies = Technology.objects.all().order_by('-name')
    return technologies


def get_base_context():
    return {
        'links': get_links(),
        'project_technologies': get_project_technologies(),
    }

# Create your views here.


def project_index(request):
    projects = Project.objects
    if not request.user.is_staff:
        projects = projects.filter(is_published=True)
    else:
        projects = projects.all()
    context = get_base_context()
    context['projects'] = projects
    return render(request, 'project_index.html', context)


def project_technology(request, technology):
    projects = Project.objects.filter(
        technologies_used__name__contains=technology
    )
    if not request.user.is_staff:
        projects = projects.filter(is_published=True)
    else:
        projects = projects.all()
    context = get_base_context()
    context['projects'] = projects
    context['technology'] = technology
    return render(request, 'project_technology.html', context)


def project_detail(request, sub_url):
    project = Project.objects.get(sub_url=sub_url)
    if not request.user.is_staff and not project.is_published:
        raise Http404
    context = get_base_context()
    context['project'] = project
    return render(request, 'project_detail.html', context)
