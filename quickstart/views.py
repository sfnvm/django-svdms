from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# class AuthorViewset(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

#     def perform_create(self, serializer):
#         serializer.save(added_by=self.request.user)


# class BookViewset(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def perform_create(self, serializer):
#         serializer.save(added_by=self.request.user)
