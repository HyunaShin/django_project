from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Comment(models.Model):
    comment_contents = models.CharField(primary_key=True, max_length = 500)
