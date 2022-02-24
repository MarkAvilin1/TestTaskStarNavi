from django.contrib.auth.models import User
from django.db import models


class Posts(models.Model):
    post = models.TextField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)


class LikeStatus(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    ls_date = models.DateTimeField(auto_now_add=True)
    postid = models.ForeignKey(Posts, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
