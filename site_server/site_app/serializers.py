from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import *


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#
# class UserActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('last_login',)
#
# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = Account
#         fields = ['email', 'username', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def save(self):
#         account = Account(
#             email=self.validated_data['email'],
#             username=self.validated_data['username']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         account.set_password(password)
#         account.save()
#         return account


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStatus
        fields = '__all__'
