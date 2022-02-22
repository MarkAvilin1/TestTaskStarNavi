from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from site_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/create_user/', UserCreateView.as_view(), name='create_user'),
    path('api/v1/login_user/', login, name='login'),
    path('api/v1/post_create/', PostCreateView.as_view()),
    path('api/v1/posts/', PostListView.as_view()),
    path('api/v1/likes/', PostLikeView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]