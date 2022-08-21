from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, MatchReport, Category
from .forms import CreateArticleForm, CreateMatchReportForm, EditArticleForm, EditMatchReportForm, CreateCategoryForm

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateMatchReportView(CreateView):
    model = MatchReport
    form_class = CreateMatchReportForm
    template_name = 'create_match_report.html'

class EditArticleView(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'edit_article.html'

class EditMatchReportView(UpdateView):
    model = MatchReport
    form_class = EditMatchReportForm
    template_name = 'edit_match_report.html'

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'create_category.html'