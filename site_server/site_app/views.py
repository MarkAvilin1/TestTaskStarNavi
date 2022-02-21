from rest_framework import generics
from rest_framework.permissions import *
from .models import Users
from .serializers import UserSerializer


class UserAPIList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminUser,)


class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminUser,)
