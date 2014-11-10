from django.views.generic import CreateView

from accounts.models import MyUserCreationForm


class Register(CreateView):
    template_name = "registration/signup.html"
    form_class = MyUserCreationForm
    success_url = "/accounts/login"

