from django.urls import path
from .views import UserRegisterView, UserEditView, CustomPasswordChangeView, StaffView, RemoveAdministratorView, AddAdministratorView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('profile/', UserEditView.as_view(), name="profile"),
    path('password/', CustomPasswordChangeView.as_view(), name="change-password"),
    path('staff/', StaffView.as_view(), name="staff"),
    path('remove-administrator/', RemoveAdministratorView, name="remove-administrator"),
    path('add-administrator/', AddAdministratorView, name="add-administrator")
]
