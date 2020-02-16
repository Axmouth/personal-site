from django.shortcuts import render
from blog.models import Post, Category


def get_blog_categories():
    categories = Category.objects.all().order_by('-name')
    return categories

def get_base_context():
    return {
        'blog_categories': get_blog_categories(),
    }

# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html', {})


def blog_index(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_on')
    context = get_base_context()
    context['posts'] = posts
    return render(request, 'blog_index.html', context)


def blog_search(request):
    """
    Display a Blog List page filtered by the search query.
    """
    query = request.GET.get('q')
    qs = Post.objects
    for word in query.split(' '):
        qs = qs.filter(title__icontains=word)
        qs = qs.filter(description__icontains=word)
        qs = qs.filter(content__icontains=word)
    posts = qs.filter(is_published=True).order_by('-created_on')
    result_number = posts.count()
    context = get_base_context()
    context['posts'] = posts
    context['result_number'] = result_number
    context['query'] = query
    return render(request, 'blog_search.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = get_base_context()
    context['category'] = category
    context['posts'] = posts
    return render(request, 'blog_category.html', context)


def blog_detail(request, sub_url):
    post = Post.objects.get(sub_url=sub_url)

    context = get_base_context()
    context['post'] = post
    return render(request, 'blog_detail.html', context)
