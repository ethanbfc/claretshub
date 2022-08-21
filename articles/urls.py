from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('create_article', CreateArticleView.as_view(), name="create-article"),
    path('create_match_report', CreateMatchReportView.as_view(), name="create-match-report"),
    path('create_player_profile', CreatePlayerProfileView.as_view(), name="create-player-profile"),
    path('article/edit/<int:pk>', EditArticleView.as_view(), name="edit-article"),
    path('match_report/edit/<int:pk>', EditMatchReportView.as_view(), name="edit-match-report"),
    path('player_profile/edit/<int:pk>', EditPlayerProfileView.as_view(), name="edit-player-profile"),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name="delete-article"),
    path('create_category', CreateCategoryView.as_view(), name="create-category")
]
