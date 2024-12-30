<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'board/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.view_count += 1
    post.save()
    
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'board/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('board:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'board/form.html', context)

@login_required
def comment_create(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get('content')
        
        if content:
            comment = Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'comment_id': comment.id,
                    'username': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                })
            
            return redirect('board:detail', pk)
    return redirect('board:detail', pk)

@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        return redirect('board:detail', pk)
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('board:detail', post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'board/form.html', context)

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            post.delete()
            return JsonResponse({'status': 'success'})
        else:
            post.delete()
            return redirect('board:index')
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
    }
    return render(request, 'board/index.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.view_count += 1
    post.save()
    
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'board/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('board:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'board/form.html', context)

@login_required
def comment_create(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get('content')
        
        if content:
            comment = Comment.objects.create(
                post=post,
                user=request.user,
                content=content
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'comment_id': comment.id,
                    'username': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
                })
            
            return redirect('board:detail', pk)
    return redirect('board:detail', pk)

@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        return redirect('board:detail', pk)
        
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('board:detail', post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'board/form.html', context)

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            post.delete()
            return JsonResponse({'status': 'success'})
        else:
            post.delete()
            return redirect('board:index')
>>>>>>> e86b7b9f37d611aad436361104d1f4cb0dea76e7
    return redirect('board:detail', pk)