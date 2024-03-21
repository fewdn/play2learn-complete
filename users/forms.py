from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

# If you want to make first and last names required on signup
# add the following to settings
# ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'
# then uncomment the following
#class SignupForm(forms.Form):
#    first_name = forms.CharField(max_length=50, required=True)
#    last_name = forms.CharField(max_length=50, required=True)

#    def signup(self, request, user):
#        user.first_name = self.cleaned_data['first_name']
#        user.last_name = self.cleaned_data['last_name']
#        user.save()

        