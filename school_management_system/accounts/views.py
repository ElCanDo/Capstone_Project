from django.shortcuts import render
from . models import CustomUser
from . serializers import CustomUserSerializer
from rest_framework import viewsets

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.object.all()
    serializer_class = CustomUserSerializer()
    