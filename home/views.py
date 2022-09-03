from django.views.generic import ListView, TemplateView
from articles.models import Article

class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-date']
    paginate_by = 10

class AboutView(TemplateView):
    template_name = 'about.html'

class JobView(TemplateView):
    template_name = 'jobs.html'

class TermsOfServiceView(TemplateView):
    template_name = 'terms_of_service.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'

class CookiePolicyView(TemplateView):
    template_name = 'cookie_policy.html'

class AccessibilityView(TemplateView):
    template_name = 'accessibility.html'

class AdvertisingView(TemplateView):
    template_name = 'advertising.html'