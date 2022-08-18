from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordChangeForm

class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('home')