from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.
class AnagramHuntScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    score = models.IntegerField()
    max_number = models.IntegerField() # number of characters in word
    time_left = models.IntegerField()  # number of seconds - game timer
    created = models.DateTimeField(auto_now_add=True) 

class MathFactsScore(models.Model):
    OPERATORS = [
        ('addition', 'addition'),
        ('subtraction', 'subtraction'),
        ('multiplication', 'multiplication'),
        ('division', 'division')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    score = models.IntegerField()
    max_number = models.IntegerField() # largest number allowed as operand
    time_left = models.IntegerField()  # number of seconds - game timer
    operator = models.CharField(max_length=50, choices=OPERATORS)
    created = models.DateTimeField(auto_now_add=True)

