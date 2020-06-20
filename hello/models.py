from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """Model representing a post."""
    title = models.CharField(max_length=25)
    content = models.CharField(max_length=350)
    def __str__(self):
        return self.title
