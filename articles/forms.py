from django import forms
from .models import Article, MatchReport, Category, PlayerProfile

# Create Forms

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'snippet', 'thumbnail', 'category', 'body', 'match_report', 'player_profile')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'match_report': forms.Select(attrs={'class': 'form-control'}),
            'player_profile': forms.Select(attrs={'class': 'form-control'})
        }

class CreateMatchReportForm(forms.ModelForm):
    class Meta:
        model = MatchReport
        fields = ('opponent', 'stadium', 'date', 'officials', 'burnley_goals', 'burnley_scorers','opponent_goals','opponent_scorers', 'burnley_team', 'opponent_team', 'possession_burnley', 'shots_burnley', 'shots_on_target_burnley', 'corners_burnley', 'fouls_burnley', 'possession_opponent', 'shots_opponent', 'shots_on_target_opponent', 'corners_opponent', 'fouls_opponent')

        widgets = {
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'officials': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_goals': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_goals': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_team': forms.Textarea(attrs={'class': 'form-control'}),
            'opponent_team': forms.Textarea(attrs={'class': 'form-control'}),
            'possession_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_on_target_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'corners_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'fouls_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'possession_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_on_target_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'corners_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'fouls_opponent': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreatePlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ('name', 'dob', 'position', 'nationality', 'international_caps_goals', 'player_stats', 'manager_stats', 'current_job')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'international_caps_goals': forms.TextInput(attrs={'class': 'form-control'}),
            'player_stats': forms.Textarea(attrs={'class': 'form-control'}),
            'manager_stats': forms.Textarea(attrs={'class': 'form-control'}),
            'current_job': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]

# Edit Forms

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'snippet', 'thumbnail', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditMatchReportForm(forms.ModelForm):
    class Meta:
        model = MatchReport
        fields = ('opponent', 'stadium', 'date', 'officials', 'burnley_goals', 'burnley_scorers','opponent_goals','opponent_scorers', 'burnley_team', 'opponent_team', 'possession_burnley', 'shots_burnley', 'shots_on_target_burnley', 'corners_burnley', 'fouls_burnley', 'possession_opponent', 'shots_opponent', 'shots_on_target_opponent', 'corners_opponent', 'fouls_opponent')

        widgets = {
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'officials': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_goals': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_goals': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_team': forms.Textarea(attrs={'class': 'form-control'}),
            'opponent_team': forms.Textarea(attrs={'class': 'form-control'}),
            'possession_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_on_target_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'corners_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'fouls_burnley': forms.TextInput(attrs={'class': 'form-control'}),
            'possession_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'shots_on_target_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'corners_opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'fouls_opponent': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditPlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile
        fields = ('name', 'dob', 'position', 'nationality', 'international_caps_goals', 'player_stats', 'manager_stats', 'current_job')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control'}),
            'international_caps_goals': forms.TextInput(attrs={'class': 'form-control'}),
            'player_stats': forms.Textarea(attrs={'class': 'form-control'}),
            'manager_stats': forms.Textarea(attrs={'class': 'form-control'}),
            'current_job': forms.TextInput(attrs={'class': 'form-control'}),
        }