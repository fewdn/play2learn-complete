from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Creating a custom User allows option of future changes
class CustomUser(AbstractUser):
    def get_absolute_url(self):
        return reverse('my-account')
