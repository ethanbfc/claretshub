from django.views.generic import ListView
from articles.models import Article

class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-date']