from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet, Ping
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


customUserViewset = CustomUserViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
})


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', customUserViewset, name='user'),
    path('ping/', Ping.as_view(), name="ping")
]
