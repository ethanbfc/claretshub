from django.urls import path
from .views import HomeView, ArticleDetailView, CreateArticleView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('create_article', CreateArticleView.as_view(), name="create-article")
]
