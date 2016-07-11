from django.contrib.auth.models import User
from django.shortcuts import render
from . import serializer,models
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets,permissions

from rest_framework.authentication import BasicAuthentication
# Create your views here.
from rest_framework import generics
from api.serializer import SignUpSerializer
from .permissions import IsAuthenticatedOrCreate

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
class TypeUserView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.TypeUserSerialzer
    queryset = models.TypeUser.objects.all()

