from django.urls import path
from .views import UserRegisterView, UserEditView, CustomPasswordChangeView, StaffView, RemoveWriterView, AddWriterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('profile/', UserEditView.as_view(), name="profile"),
    path('password/', CustomPasswordChangeView.as_view(), name="change-password"),
    path('staff/', StaffView.as_view(), name="staff"),
    path('remove-writer/', RemoveWriterView, name="remove-writer"),
    path('add-writer/', AddWriterView, name="add-writer")
]
