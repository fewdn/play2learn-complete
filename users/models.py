from django.contrib.auth.models import AbstractUser
from django.db import models

# Creating a custom User allows option of future changes
class CustomUser(AbstractUser):
    pass
