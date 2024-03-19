from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
        