from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")

class Article(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-details", args=(str(self.id)))