from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .forms import RegisterForm, EditProfileForm, PasswordChangeForm, UsernameForm
from .models import Account

class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('home')

# Manage Staff

class StaffView(ListView):
    model = User
    template_name = 'manage_staff.html'

def RemoveAdministratorView(request):
    account = get_object_or_404(Account, user=request.POST.get('user_id'))
    account.administrator = False
    account.save(update_fields=["administrator"])
    messages.success(request, (f"The user '{account.user.username}' has been removed as a writer."))
    return HttpResponseRedirect(reverse('staff'))

def AddAdministratorView(request):
    if (request.method == "POST"):
        form = UsernameForm(request.POST or None)
        if (User.objects.filter(username=request.POST['username']).exists()):
            this_user = User.objects.get(username=request.POST['username'])
            account = get_object_or_404(Account, user=this_user)
            account.administrator = True
            account.save(update_fields=["administrator"])
            messages.success(request, (f"The user '{this_user.username}' has been added as a writer."))
        else:
            messages.success(request, (f"The user with the username '{request.POST['username']}' cannot be found."))
    return HttpResponseRedirect(reverse('staff'))