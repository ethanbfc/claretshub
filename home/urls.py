from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('news/', NewsView.as_view(), name="news"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView, name="contact"),
    path('faq/', FAQView.as_view(), name="faq"),
    path('jobs/', JobView.as_view(), name="jobs"),
    path('terms-of-service/', TermsOfServiceView.as_view(), name="terms-of-service"),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name="privacy-policy"),
    path('cookie-policy/', CookiePolicyView.as_view(), name="cookie-policy"),
    path('accessibility/', AccessibilityView.as_view(), name="accessibility"),
    path('advertising/', AdvertisingView.as_view(), name="advertising")
]
