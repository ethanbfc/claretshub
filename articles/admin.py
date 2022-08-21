from django.contrib import admin
from .models import Article, MatchReport, PlayerProfile, Category

admin.site.register(Article)
admin.site.register(MatchReport)
admin.site.register(PlayerProfile)
admin.site.register(Category)