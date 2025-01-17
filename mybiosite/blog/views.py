from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseNotFound, Http404
from blog.models import Post, Category
from home_page.models import Link


def get_blog_categories():
    categories = Category.objects.all().order_by('-name')
    return categories


def get_links():
    links = Link.objects.all().order_by('-name')
    return links


def get_base_context():
    return {
        'blog_categories': get_blog_categories(),
        'links': get_links(),
    }

# Create your views here.


def hello_world(request):
    return render(request, 'hello_world.html', {})


def blog_index(request):
    """
    Display a Blog List page ordered by most recent.
    """
    posts = Post.objects.order_by('-created_on')
    if not request.user.is_staff:
        posts = posts.filter(is_published=True)
    context = get_base_context()
    result_number = posts.count()
    context['result_number'] = result_number
    context['posts'] = posts
    return render(request, 'blog_index.html', context)


def blog_search(request):
    """
    Display a Blog List page filtered by the search query.
    """
    query = request.GET.get('q')
    qs = Post.objects
    for word in query.split(' '):
        qs = qs.filter(Q(title__icontains=word) | Q(description__icontains=word) | Q(content__icontains=word))
    if not request.user.is_staff:
        qs = qs.filter(is_published=True)
    posts = qs.order_by('-created_on')
    context = get_base_context()
    context['query'] = query
    context['posts'] = posts
    result_number = posts.count()
    context['result_number'] = result_number
    return render(request, 'blog_search.html', context)


def blog_category(request, category):
    """
    Display a Blog List page filtered by the a category.
    """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    if not request.user.is_staff:
        posts = posts.filter(is_published=True)
    context = get_base_context()
    result_number = posts.count()
    context['result_number'] = result_number
    context['category'] = category
    context['posts'] = posts
    return render(request, 'blog_category.html', context)


def blog_detail(request, sub_url):
    """
    Display a Blog Post with its comments.
    """
    post = Post.objects.get(sub_url=sub_url)
    if not request.user.is_staff and not post.is_published:
        raise Http404
    context = get_base_context()
    context['post'] = post
    return render(request, 'blog_detail.html', context)
