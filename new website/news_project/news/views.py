from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Article
from .forms import CustomUserCreationForm # Use the custom form

# A custom mixin to check for superuser status
class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        # Start with all articles ordered by publication date
        object_list = self.model.objects.all().order_by('-pub_date')
        if query:
            # If a search query is present, filter the list
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return object_list

    def get_context_data(self, **kwargs):
        # Pass the search query back to the template to display in the search bar
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content', 'image']

class ArticleDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm # Use the custom form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'