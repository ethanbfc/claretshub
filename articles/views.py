from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
from .forms import CreateForm, EditForm

class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-date']

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

class CreateArticleView(CreateView):
    model = Article
    form_class = CreateForm
    template_name = 'create_article.html'

class EditArticleView(UpdateView):
    model = Article
    form_class = EditForm
    template_name = 'edit_article.html'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')