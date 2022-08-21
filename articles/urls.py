from django.urls import path
from .views import HomeView, ArticleDetailView, CreateArticleView, CreateMatchReportView, EditArticleView, EditMatchReportView, DeleteArticleView, CreateCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('create_article', CreateArticleView.as_view(), name="create-article"),
    path('create_match_report', CreateMatchReportView.as_view(), name="create-match-report"),
    path('article/edit/<int:pk>', EditArticleView.as_view(), name="edit-article"),
    path('match_report/edit/<int:pk>', EditMatchReportView.as_view(), name="edit-match-report"),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name="delete-article"),
    path('create_category', CreateCategoryView.as_view(), name="create-category")
]
