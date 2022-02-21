from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.admin import User
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Posts(models.Model):
    post = models.TextField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)


class LikesStatus(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    ls_date = models.DateTimeField(auto_now_add=True)
    postid = models.ForeignKey(Posts, on_delete=models.CASCADE)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
