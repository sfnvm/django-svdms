from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    password = serializers.CharField(source='user.password', read_only=True)
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = CustomUser
        fields = (
            'id', 'username', 'password', 'email', 'first_name', 'last_name',
            'code', 'idcard', 'phone_number', 'address', 'date_of_birth', 'gender'
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)

        customUser = CustomUser.objects.create(user=user, **validated_data)
        return customUser

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        # update User
        for attr, value in user_data.items():
            setattr(instance, attr, value)
        # update CustomUser
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
