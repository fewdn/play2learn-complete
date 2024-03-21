import json
from django.http import JsonResponse
from typing import Any
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from reviews.models import Review
from games.models import AnagramHuntScore, MathFactsScore

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
    
class AnagramHuntScoresView(TemplateView):
    template_name = "games/anagram-hunt-scores.html"
    # order descending from highest to lowest score

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scores = AnagramHuntScore.objects.order_by("-score")
        if scores.count() > 0:
            context['scores'] = scores
        return context

class AnagramHuntUserScoresView(LoginRequiredMixin, TemplateView):
    template_name = "games/anagram-hunt-user-scores.html"
    # login_url = "/login" w/o defaults to settings.LOGIN_URL (login_url is deprecated and removed in Django 5)
    # filter by user
    # order descending from highest to lowest score
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scores = AnagramHuntScore.objects.filter(user=self.request.user).order_by("-score")
        if scores.count() > 0:
            context['scores'] = scores
        return context

class MathFactsScoresView(TemplateView):
    template_name = "games/math-facts-scores.html"
    # order from highest to lowest score

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scores = MathFactsScore.objects.order_by("-score")
        if scores.count() > 0:
            context['scores'] = scores
        return context

class MathFactsUserScoresView(LoginRequiredMixin, TemplateView):
    template_name = "games/math-facts-user-scores.html"
    # login_url = "/login" w/o defaults to settings.LOGIN_URL (login_url is deprecated and removed in Django 5)

    # filter by current logged in user
    # order descending from highest to lowest score 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scores = MathFactsScore.objects.filter(user=self.request.user).order_by("-score")
        if scores.count() > 0:
            context['scores'] = scores
        return context


# record Anagram Hunt Scores
# field values : score, user, time_left, max_number (of letters)
def record_anagram_hunt_score(request):

    # Only record scores for logged in users
    if request.user.is_authenticated:
        data = json.loads(request.body)
        user = request.user
        score = data['score']
        time_left = data['time_left']
        max_number = data['max_number']
    
        new_score = AnagramHuntScore(user=user, score=score, time_left=time_left, max_number=max_number)
        new_score.save()
    
    response = {
        "success": True
    }

    return JsonResponse(response)

# record Math Facts Scores
# field values = score, user, time_left, max_number (highest number), operator (addition, subtraction, etc)
def record_math_facts_score(request):

    # Only record scores for logged in users
    if request.user.is_authenticated:
        data = json.loads(request.body)
        user = request.user
        score = data['score']
        time_left = data['time_left']
        max_number = data['max_number']
        operator = data['operator']
    
        new_score = MathFactsScore(user=user, score=score, time_left=time_left, max_number=max_number, operator=operator)
        new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)