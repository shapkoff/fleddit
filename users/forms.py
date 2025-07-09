from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None


class ChangeUserInfoForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        