from blog.models import Post, Page
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

PER_PAGE = 9

# Pagina inicial
def index(request):
    posts = Post.objects.filter(is_published=True)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


# Posts por autor
def created_by(request, author_pk):
    posts = Post.objects.filter(is_published=True)\
        .filter(created_by__pk=author_pk)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


# Posts por categoria
def category(request, slug):
    posts = Post.objects.filter(is_published=True)\
        .filter(category__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


# Posts por tag
def tag(request, slug):
    posts = Post.objects.filter(is_published=True)\
        .filter(tags__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


# Sistema de busca
def search(request):
    search_value = request.GET.get('search', '').strip()

    posts = (
        Post.objects.filter(is_published=True)
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[:PER_PAGE]
    )

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': posts,
            'search_value': search_value,
        }
    )


# Páginas estáticas
def page(request, slug):
    page = (
        Page.objects
        .filter(is_published=True)
        .filter(slug=slug)
        .first()
    )

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page,
        }
    )



# Conteúdo do post
def post(request, slug):
    post = (Post.objects.filter(is_published=True)
            .filter(slug=slug)
            .first()
    )

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
        }
    )