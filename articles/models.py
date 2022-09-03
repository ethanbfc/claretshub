from distutils.command.bdist import show_formats
from sqlite3 import converters
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
    officials = models.CharField(max_length=255)
    burnley_goals = models.PositiveSmallIntegerField()
    opponent_goals = models.PositiveSmallIntegerField()
    burnley_scorers = models.CharField(max_length=255)
    opponent_scorers = models.CharField(max_length=255)
    burnley_team = RichTextField()
    opponent_team = RichTextField()
    # Stats - Burnley
    possession_burnley = models.PositiveSmallIntegerField()
    shots_burnley = models.PositiveSmallIntegerField()
    shots_on_target_burnley = models.PositiveSmallIntegerField()
    corners_burnley = models.PositiveSmallIntegerField()
    fouls_burnley = models.PositiveSmallIntegerField()
    # Stats - Opponent
    possession_opponent = models.PositiveSmallIntegerField()
    shots_opponent = models.PositiveSmallIntegerField()
    shots_on_target_opponent = models.PositiveSmallIntegerField()
    corners_opponent = models.PositiveSmallIntegerField()
    fouls_opponent = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.opponent + " (" + self.date.strftime("%Y-%m-%d") + ")")

    def get_absolute_url(self):
        return reverse("create-article")

class PlayerProfile(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    position = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    international_caps_goals = models.CharField(max_length=30)
    player_stats = RichTextField()
    manager_stats = RichTextField(null=True, blank=True)
    current_job = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("create-article")

class Article(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='images/')
    banner = models.ImageField(upload_to='images/', null=True, blank=True)
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