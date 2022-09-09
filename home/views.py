from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.core.mail import send_mail, BadHeaderError
from articles.models import Article
from .forms import ContactForm

class HomeView(ListView):
    model = Article
    template_name = 'index.html'
    ordering = ['-date']
    paginate_by = 10

class NewsView(ListView):
    model = Article
    template_name = 'news.html'
    ordering = ['-date']
    paginate_by = 10

def ContactView(request):
    if (request.method == "GET"):
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(f"Contact Form Query: {request.POST['name']}", request.POST['message'], request.POST['email'], ["claretshub@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.success(request, ("Thank you for your email. A member of our team will review your message and reply within the next week."))
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})

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