from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Article

# A custom mixin to check for group membership
class GroupRequiredMixin(UserPassesTestMixin):
    group_required = None

    def test_func(self):
        # Check if the user is authenticated and in the required group
        if not self.request.user.is_authenticated:
            return False
        return self.request.user.groups.filter(name=self.group_required).exists()

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    ordering = ['-pub_date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content', 'image']
    group_required = 'Authors' # Specify the required group name

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content', 'image']

    def test_func(self):
        # Only the original author can update the article
        article = self.get_object()
        return self.request.user == article.author

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        # Only the original author can delete the article
        article = self.get_object()
        return self.request.user == article.author

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
