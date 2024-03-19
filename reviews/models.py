from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    review = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.review