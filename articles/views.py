from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, MatchReport, PlayerProfile, Category
from .forms import CreateArticleForm, CreateMatchReportForm, CreatePlayerProfileForm, CreateCategoryForm, EditArticleForm, EditMatchReportForm, EditPlayerProfileForm

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['articles_list'] = Article.objects.all().order_by('-date')[:3]
        return context

# Create Views

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

class CreatePlayerProfileView(CreateView):
    model = PlayerProfile
    form_class = CreatePlayerProfileForm
    template_name = 'create_player_profile.html'

class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'create_category.html'

# Edit Views

class EditArticleView(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'edit_article.html'

class EditMatchReportView(UpdateView):
    model = MatchReport
    form_class = EditMatchReportForm
    template_name = 'edit_match_report.html'

class EditPlayerProfileView(UpdateView):
    model = PlayerProfile
    form_class = EditPlayerProfileForm
    template_name = 'edit_player_profile.html'

# Delete Views

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')