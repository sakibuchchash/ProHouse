from django.shortcuts import render
from ..models import Posts,Contests
from ..forms import PostForm,ContestForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def index(request):

    posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    by = Posts.objects.all        
    return render(request, 'index.html', {'posts': posts,'by':by})


def details(request,pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'details.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Posts, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save() 
            return redirect('details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def contest(request):
    posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    by = Posts.objects.all        
    return render(request, 'contest.html', {'posts': posts,'by':by})


def condetails(request,pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'condetails.html', {'post': post})


def con_new(request):
    if request.method == "POST":
        form = ContestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publisher = request.user
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = ContestForm()
    return render(request, 'con_new.html', {'form': form})

def con_edit(request, pk):
    post = get_object_or_404(Contests, pk=pk)

    if request.method == "POST":
        form = ContestForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.publisher = request.user
            post.save() 
            return redirect('details', pk=post.pk)
    else:
        form = ContestForm(instance=post)
    return render(request, 'con_new.html', {'form': form}) 


