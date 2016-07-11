from django.contrib.auth.models import User

__author__ = 'AHMAD'
from rest_framework import serializers,permissions
from . import models
from rest_framework.response import Response
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from rest_framework import serializers

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        write_only_fields = ('password',)
class TypeUserSerialzer(serializers.ModelSerializer):
    class Meta:
        model=models.TypeUser
        fields='__all__'