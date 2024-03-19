from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from .models import AnagramHuntScore, MathFactsScore

# Register your models here.
@admin.register(AnagramHuntScore)
class AnagramHuntScoreAdmin(admin.ModelAdmin):
    model = AnagramHuntScore
    list_display = ['user', 'score', 'max_number', 'created']

@admin.register(MathFactsScore)
class MathFactsScoreAdmin(admin.ModelAdmin):
    model = MathFactsScore
    list_display = ['user', 'score', 'max_number', 'operator', 'created']
