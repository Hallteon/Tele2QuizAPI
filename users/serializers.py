from urllib import request
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'nickname', 'firstname', 'lastname', 'age', 'phone_number', 'password')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'nickname', 'firstname', 'lastname', 'age', 'phone_number')