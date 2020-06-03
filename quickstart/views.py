from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import SalesManager
from .serializers import SalesManagerSerializer


class SalesManagerViewSet(viewsets.ModelViewSet):
    queryset = SalesManager.objects.all()
    serializer_class = SalesManagerSerializer
