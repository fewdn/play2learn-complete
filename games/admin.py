from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import AnagramHuntScore, MathFactsScore

# Register your models here.
@admin.register(AnagramHuntScore)
class AnagramHuntScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'max_number', 'time_left', 'created']
    fields = ['user', 'score', 'max_number', 'time_left']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing if existing object
            return ('created')
        return()

@admin.register(MathFactsScore)
class MathFactsScoreAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'max_number', 'operator', 'created']
    fields = ['user', 'score', 'max_number', 'operator','time_left']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing if existing object
            return ('created')
        return()