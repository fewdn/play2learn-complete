from django import forms

class ContactUsForm(forms.Form):
    first_name = forms.CharField(
        widget = forms.TextInput(attrs={'autofocus':True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField(max_length=80, widget=forms.Textarea)