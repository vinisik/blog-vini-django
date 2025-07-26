from blog.models import Post, Page
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

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
    user = User.objects.filter(pk=author_pk).first()

    if user is None:
        raise Http404()

    posts = Post.objects.filter(is_published=True)\
        .filter(created_by__pk=author_pk)
    user_full_name = user.username

    if user.first_name:
        user_full_name = f'{user.first_name} {user.last_name}'
    page_title = 'Posts de ' + user_full_name + ' - '
    page_title_main = 'Posts de ' + user_full_name

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
            'page_title_main': page_title_main,
        }
    )



# Posts por categoria
def category(request, slug):
    posts = Post.objects.filter(is_published=True)\
        .filter(category__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f'{page_obj[0].category.name} - Categoria - '
    page_title_main = f'Categorias > {page_obj[0].category.name}'

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
            'page_title_main': page_title_main,
        }
    )


# Posts por tag
def tag(request, slug):
    posts = Post.objects.filter(is_published=True)\
        .filter(tags__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f'{page_obj[0].tags.first().name} - Tag - '
    page_title_main = f'Tags > {page_obj[0].tags.first().name}'

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
            'page_title_main': page_title_main,
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
    page_obj = (
        Page.objects
        .filter(is_published=True)
        .filter(slug=slug)
        .first()
    )

    if page_obj is None:
        raise Http404()

    page_title = f'{page_obj.title} - '

    return render(
        request,
        'blog/pages/page.html',
        {
            'page': page_obj,
            'page_title': page_title,
        }
    )


# Conteúdo do post
def post(request, slug):
    post_obj = (
        Post.objects.filter(is_published=True)
        .filter(slug=slug)
        .first()
    )

    if post_obj is None:
        raise Http404()

    page_title = f'{post_obj.title} - '

    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post_obj,
            'page_title': page_title,
        }
    )