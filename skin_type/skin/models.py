from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserName(models.Model):
    user_name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.user_name

class Comment(models.Model):
    comment_id =  models.AutoField(primary_key=True)
    comment_contents = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
#
# class first_question(models.Model):
#     question = models.ForeignKey(UserName)
#
#
# ########################################
# class Comment(models.Model):
#     comment = models.TextField(max_length = 1000)
#
#     def __str__(self):
#         return self.comment
#
# class StarRate(models.Model):
#     star_rate = models.TextField(max_length=1)
