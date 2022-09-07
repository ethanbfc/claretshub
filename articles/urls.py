from django.urls import path
from .views import *

urlpatterns = [
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('create-article', CreateArticleView.as_view(), name="create-article"),
    path('create-match-report', CreateMatchReportView.as_view(), name="create-match-report"),
    path('create-player-profile', CreatePlayerProfileView.as_view(), name="create-player-profile"),
    path('article/edit/<int:pk>', EditArticleView.as_view(), name="edit-article"),
    path('match-report/edit/<int:pk>', EditMatchReportView.as_view(), name="edit-match-report"),
    path('player-profile/edit/<int:pk>', EditPlayerProfileView.as_view(), name="edit-player-profile"),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name="delete-article"),
    path('categories', CategoryView.as_view(), name="categories"),
    path('remove-category/', RemoveCategoryView, name="remove-category"),
    path('create-category', CreateCategoryView, name="create-category")
]
