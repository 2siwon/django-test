from django.shortcuts import render

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            Post.object.create(
                title=form.cleaned_data['title'],
                photo=form.cleaned_data['photo'],
                content=form.cleaned_data['content'],
                created_date=form.cleaned_data['created_date'],
            )

            return render(request, 'post/post_list.html')

    post_form = PostForm()

    context = {
        'post_form': post_form
    }

    return render(request, 'post/post_create.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'post/post_delete.html', context)
