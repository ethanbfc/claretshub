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

class MatchReport(models.Model):
    opponent = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now)
    stadium = models.CharField(max_length=100)
    referee = models.CharField(max_length=255)
    score = models.CharField(max_length=10)
    burnley_scorers = models.CharField(max_length=255)
    opponent_scorers = models.CharField(max_length=255)
    burnley_team = RichTextField()
    opponent_team = RichTextField()
    stats = RichTextField()

    def __str__(self):
        return str(self.opponent + " (" + self.date.strftime("%Y-%m-%d") + ")")

    def get_absolute_url(self):
        return reverse("create-article")

class PlayerProfile(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField()
    nationality = models.CharField(max_length=100)
    stats = RichTextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("create-article")

class Article(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = RichTextField(default="Default Body Text")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    match_report = models.OneToOneField(MatchReport, on_delete=models.CASCADE, null=True, blank=True)
    player_profile = models.OneToOneField(PlayerProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-details", kwargs={'pk': self.id})