from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import ArticleForm

class HomeView(ListView):
    model = Article
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'create_article.html'