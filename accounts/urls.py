from django.urls import path
from .views import SignUpView, ProfileUpdateView, CustomLoginView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("login/", CustomLoginView.as_view(), name="login"),
]