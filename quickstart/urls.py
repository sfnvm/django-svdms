from django.urls import path, include
from rest_framework import routers
from .views import SalesManagerViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


salesManagerViewset = SalesManagerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('sales_manager/', salesManagerViewset, name='sales_manager'),
]
