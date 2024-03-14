from django.shortcuts import render

from .models import Post


app_name = 'blog'

# Create your views here.
def index(request):
    all_posts = Post.objects.all()

    for p in all_posts:
        print(p)
    content = {
        'all_posts': all_posts
    }

    return render(request, 'blog/index.html', content)


def detail(request, post_id):

    post = Post.objects.get(pk=post_id)

    content = {
        'post': post
    }

    return render(request, 'blog/detail.html', content)