from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Category
from .forms import CreateArticleForm, EditArticleForm, CreateCategoryForm

class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

class CreateArticleView(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'create_article.html'

class EditArticleView(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'edit_article.html'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'create_category.html'