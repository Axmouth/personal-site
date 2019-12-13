from django.shortcuts import render
from blog.models import Post


# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html', {})


def blog_index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, sub_url):
    post = Post.objects.get(sub_url=sub_url)

    context = {
        "post": post,
    }
    return render(request, "blog_detail.html", context)
