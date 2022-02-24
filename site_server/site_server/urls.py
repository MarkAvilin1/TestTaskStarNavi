from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from knox import views as knox_views
from site_app.views import *
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/register/', RegisterAPI.as_view(), name='register'),
    path('api/v1/login/', LoginAPI.as_view(), name='login'),
    path('api/v1/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/v1/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/v1/activity/', UserLastActivity.as_view(), name='user_last_activity'),

    path('api/v1/create_post/', PostCreateView.as_view(), name='create_post'),
    path('api/v1/posts/', PostListView.as_view(), name='posts'),
    path('api/v1/likes/', PostLikeView.as_view(), name='like_status'),
    path('api/v1/put_likes/', PostLikeCreateView.as_view(), name='put_likes'),
    path('api/v1/post/analytics/date_from=<date_from>&date_to=<date_to>/', PostAnalyticsView.as_view(), name='analytics'),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
