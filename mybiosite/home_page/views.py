from django.shortcuts import render
from projects.models import Project
from home_page.models import Link, TextBody


def get_links():
    links = Link.objects.all().order_by('-name')
    return links


def get_introduction():
    intro = TextBody.objects.filter(name='introduction')
    if not intro:
        return ''
    else:
        return intro[0]


def get_base_context():
    return {
        'links': get_links(),
        'introduction': get_introduction(),
    }


# Create your views here.

def home_page(request):
    context = get_base_context()
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'home_page.html', context)


def my_page(request):
    context = get_base_context()
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'mypage.html', context)
