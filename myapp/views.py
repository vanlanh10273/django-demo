from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.filter(status='approved').order_by("-created_at")[:5]

    return render(request, 'index.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('posts:detail', post_id=post.id)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'detail.html', {'post': post, 'comments': comments, 'form': form})

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)


def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

