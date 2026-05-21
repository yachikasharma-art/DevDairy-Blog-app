from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from .forms import PostForm
from django.views import View
from django.views.generic import DetailView, ListView

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.all()
class PostDetails(DetailView):
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'
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
from .forms import PostForm
from django.views import View

class AddPostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/add_post.html', {'form': form})
        
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'blog/add_post.html', {'form': form})
