from rest_framework import generics, permissions
from rest_framework.utils import json
from django.http import HttpResponse
from .serializers import *


class PostCreateView(generics.CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostLikeCreateView(generics.CreateAPIView):
    queryset = LikeStatus.objects.all()
    serializer_class = LikeSerializer


class PostLikeView(generics.ListAPIView):
    queryset = LikeStatus.objects.all()
    serializer_class = LikeSerializer


class PostAnalyticsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        posts_analytic = Posts.objects.filter(posts_published__range=[kwargs['date_from'], kwargs['date_to']])
        if len(posts_analytic) > 0:
            mimetype = 'application/json'
            return HttpResponse(json.dumps({'posts by period': len(posts_analytic)}), mimetype)
        else:
            return self.list(request, *args, [{}])
