from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Teacher
from .serializers import TeacherSerializer

#Teacher ViewSet for API endpoints
class TeacherViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication] # Token-based authentication

    permission_classes = [IsAuthenticated] # Only authenticated users can access

    queryset = Teacher.objects.all() # Queryset of all Teacher objects
    
    serializer_class = TeacherSerializer # Serializer for Teacher model
