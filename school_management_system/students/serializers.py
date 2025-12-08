from rest_framework import serializers
from accounts.serializers import CustomUserSerializer 
from .models import Student

# Serializer for the Student model
class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Nested serializer for the related CustomUser model

    class Meta:
        model = Student
        fields = '__all__'   # All Fields to be included in the serialization

        read_only_fields = ['enrollment_date']  # enrollment_date is read-only