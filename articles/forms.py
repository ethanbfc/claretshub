from django import forms
from .models import Article, MatchReport, Category

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'snippet', 'thumbnail', 'category', 'body', 'match_report', 'player_profile')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'match_report': forms.Select(attrs={'class': 'form-control'}),
            'player_profile': forms.Select(attrs={'class': 'form-control'})
        }

class CreateMatchReportForm(forms.ModelForm):
    class Meta:
        model = MatchReport
        fields = ('opponent', 'stadium', 'date', 'referee', 'score', 'burnley_scorers', 'opponent_scorers', 'burnley_team', 'opponent_team', 'stats')

        widgets = {
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(),
            'referee': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_team': forms.Textarea(attrs={'class': 'form-control'}),
            'opponent_team': forms.Textarea(attrs={'class': 'form-control'}),
            'stats': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditMatchReportForm(forms.ModelForm):
    class Meta:
        model = MatchReport
        fields = ('opponent', 'stadium', 'date', 'referee', 'score', 'burnley_scorers', 'opponent_scorers', 'burnley_team', 'opponent_team', 'stats')

        widgets = {
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'stadium': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(),
            'referee': forms.TextInput(attrs={'class': 'form-control'}),
            'score': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_scorers': forms.TextInput(attrs={'class': 'form-control'}),
            'burnley_team': forms.Textarea(attrs={'class': 'form-control'}),
            'opponent_team': forms.Textarea(attrs={'class': 'form-control'}),
            'stats': forms.Textarea(attrs={'class': 'form-control'})
        }

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }