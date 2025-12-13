from rest_framework import serializers
from .models import CustomUser

"""Serializer for the CustomUser model"""

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 
                  'username', 'first_name', 
                  'last_name', 
                  'email', 
                  'role'] 
        
        read_only_fields = ['id', 'role']