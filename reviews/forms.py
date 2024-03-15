from django import forms
from django.forms import ModelForm, Textarea

from .models import Review

class ReviewCreateForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        # exclude = ['featured', 'created'] only needed if fields = "__all__"
        widgets = {
            'review': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
        }
        help_texts = {
            'review': 'Please do not use dirty words.'
        }