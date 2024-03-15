from typing import Any
from django.shortcuts import render

from reviews.models import Review

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(featured=True)
        if reviews.count() > 0:
            context['reviews'] = reviews
        return context
