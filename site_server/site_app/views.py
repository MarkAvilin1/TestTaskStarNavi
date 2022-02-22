from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

from site_server import settings
from .models import *
from .serializers import *


class UserCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    queryset = Users.objects.all()
    serializer_class = UserSerializer

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


@csrf_exempt
@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    user = Users.objects.get(username=username, password=password)
    if request.user.is_authenticated:
        print("user is authenticated")
    else:
        print("User is not authenticated")
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class PostCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostLikeView(generics.CreateAPIView):
    queryset = LikeStatus.objects.all()
    serializer_class = LikeSerializer
