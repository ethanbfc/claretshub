from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    body = models.TextField()
    type = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-details", args=(str(self.id)))
    