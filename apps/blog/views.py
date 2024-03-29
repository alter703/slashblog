from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm

app_name = 'blog'

# Create your views here.
def index(request):
    all_posts = Post.objects.all()

    context = {
        'all_posts': all_posts,
        'created_form': PostForm()
    }

    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/detail.html', context)


def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            this_post = form.save(commit=False)
            this_post.author = request.user
            this_post.save()

            return redirect('blog:detail', post_id=this_post.id)
        