from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError

from projects.models import Project
from home_page.models import Link, TextBody
from home_page.forms import ContactForm

from mybiosite.settings import EMAIL_HOST


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


def contact_me(request):
    context = get_base_context()
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['contact@giorgosnikolop.info'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    context['form'] = form
    return render(request, 'contact_me.html', context)


def contact_success(request):
    context = get_base_context()
    return render(request, 'contact_success.html', context)


def my_page(request):
    context = get_base_context()
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'mypage.html', context)
