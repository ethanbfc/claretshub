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
    burnley_team = RichTextField(default="<p><small>GK</small>:<br/><small>LB</small>:<br/><small>CB</small>:<br/><small>CB</small>:<br/><small>RB</small>:<br/><small>CDM</small>:<br/><small>CM</small>:<br/><small>CM</small>:<br/><small>LW</small>:<br/><small>RW</small>:<br/><small>ST</small>:</p>")
    opponent_team = RichTextField(default="<p><small>GK</small>:<br/><small>LB</small>:<br/><small>CB</small>:<br/><small>CB</small>:<br/><small>RB</small>:<br/><small>CDM</small>:<br/><small>CM</small>:<br/><small>CM</small>:<br/><small>LW</small>:<br/><small>RW</small>:<br/><small>ST</small>:</p>")
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
    dob = models.DateField(default=datetime.now)
    position = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    international_caps_goals = models.CharField(max_length=30)
    player_stats = RichTextField(default="<table class=\"table table-bordered\"><thead><tr><th>Team</th><th>Season</th><th>League</th><th>Apps</th><th>Goals</th><th>Assists</th><th>Clean Sheets</th></tr></thead><tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>")
    manager_stats = RichTextField(null=True, blank=True, default="<table class=\"table table-bordered\"><thead><tr><th>Team</th><th>Start</th><th>End</th><th>Played</th><th>Win</th><th>Draw</th><th>Lose</th></tr></thead><tbody><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>")
    current_job = models.CharField(max_length=100, default="N/A")

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
    body = RichTextField(default="Enter the article body here...")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    match_report = models.OneToOneField(MatchReport, on_delete=models.CASCADE, null=True, blank=True)
    player_profile = models.OneToOneField(PlayerProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article-details", kwargs={'pk': self.id})