from rest_framework import serializers
# from .models import Author, Book


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['id', 'name', 'added_by', 'created_date']


# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.HyperlinkedRelatedField (
#         read_only=True,
#         view_name='api:authors'
#     )

#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'description',
#                   'created_date', 'author', 'added_by']
