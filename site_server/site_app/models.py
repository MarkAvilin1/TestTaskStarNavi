from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    last_name = None
    first_name = None
    # email = None
    user_permissions = '__all__'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Posts(models.Model):
    post = models.TextField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)


class LikeStatus(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    ls_date = models.DateTimeField(auto_now_add=True)
    postid = models.ForeignKey(Posts, on_delete=models.CASCADE)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
