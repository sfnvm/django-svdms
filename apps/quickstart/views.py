from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.renderers import JSONRenderer

from utils.JSONRenderer import EmberJSONRenderer

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    renderer_classes = (EmberJSONRenderer, )

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class Ping(APIView):
    renderer_classes = (EmberJSONRenderer, )

    def get(self, request, format=None):
        return Response('pong!')
