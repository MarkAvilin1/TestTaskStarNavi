from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('last_login',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStatus
        fields = '__all__'


