from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class MyUserCreationForm(UserCreationForm):
    """
    Custom Signup Form adding email field & condition checkbox
    """
    email = forms.EmailField(required=True)
    conditions = forms.BooleanField(required=True,
                                    error_messages={'required': 'Vous devez accepter les conditions generales.'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "conditions")

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user