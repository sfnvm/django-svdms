from django.urls import path, include
from rest_framework import routers
# from .views import BookViewset, AuthorViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

# bookViewset = BookViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# authorViewset = AuthorViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('authors/', authorViewset, name='authors'),
    # path('books/', bookViewset, name='books'),
]
