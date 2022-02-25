from rest_framework import serializers
from .models import *

# Posts serializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

# Like status serializer
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStatus
        fields = '__all__'
