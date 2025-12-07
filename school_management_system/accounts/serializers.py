from rest_framework import serializers
from .models import CustomUser

# Serializer for the CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 
                  'username', 'first_name', 
                  'last_name', 
                  'email', 
                  'role'] # Fields to be included in the serialization
        
        read_only_fields = ['id', 'role'] # id and role are read-only