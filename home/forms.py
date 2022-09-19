from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    categories = [('Bug Report', 'Bug Report'), ('Question', 'Question'), ('Sponsor', 'Sponsor Clarets Hub'), ('Privacy / Data Request', 'Privacy / Data Request'), ('Other', 'Other')]
    category = forms.ChoiceField(choices=categories, widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))