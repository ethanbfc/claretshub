from django.urls import path
from .views import HomeView, ArticleDetailView, CreateArticleView, EditArticleView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('create_article', CreateArticleView.as_view(), name="create-article"),
    path('article/edit/<int:pk>', EditArticleView.as_view(), name="edit-article")
]
