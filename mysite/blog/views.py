from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login


def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_details(request,pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'blog/details.html',{'post':post})
def category_view(request, category):
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html', {'posts': posts})
def contact(request):
    return render(request, 'blog/contact.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to DevDiary!')
            return redirect('post_list')
        else:
            print(form.errors)  # ye add kar
            messages.error(request, 'Registration failed. Please check the details.')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'image']

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})
