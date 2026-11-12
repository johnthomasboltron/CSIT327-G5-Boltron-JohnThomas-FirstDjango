from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .forms import BootstrapAuthenticationForm


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Your CampusConnect account was created successfully! You can now log in."

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "accounts/profile.html"

    form_class = ProfileUpdateForm

    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

class CustomLoginView(LoginView):
    authentication_form = BootstrapAuthenticationForm
    template_name = "registration/login.html"