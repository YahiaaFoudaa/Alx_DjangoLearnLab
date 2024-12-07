from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, loginForm, ProfileForm, PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,}
    return render(request, 'blog/base.html')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = loginForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance = user)
        if form.is_valid():
            form.save()
            messages.success(request , 'profile updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance = user)
    return render(request , 'blog/profile.html' , {'form':form})

class CreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ListView(ListView):
    model = Post
    template_name = 'blog/blogs.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

class DetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(id = self.kwargs['pk'])
    
class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        """
        Additional logic (if needed) before saving the form.
        """
        form.instance.author = self.request.user  # Ensure the author remains the same
        return super().form_valid(form)

    def test_func(self):
        """
        Restrict access to the original author of the post.
        """
        post = self.get_object()
        return post.author == self.request.user


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for confirmation
    success_url = reverse_lazy('blogs')  # Redirect to the post list after deletion

    def test_func(self):
        """
        Restrict delete access to the author of the post.
        """
        post = self.get_object()
        return post.author == self.request.user


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    

    def form_valid(self, form):
        post = get_object_or_404(Post , id = self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse('post_detail' , kwargs={'pk':post_id})
    
class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        post = get_object_or_404(Post , id = self.kwargs['post_id'])
        return Comment.objects.filter(post = post)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post , id = self.kwargs['post_id'])
        return context
    
class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('blogs')

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
    
class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('blogs')

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
                )
        return Post.objects.all()
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        return Post.objects.filter(tags__name__in=[tag])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag')
        return context