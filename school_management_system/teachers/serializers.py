from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import Teacher

# Serializer for Teacher model
class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Nested serializer for the related CustomUser model
    class Meta:
        model = Teacher
        fields = '__all__'  # Serialize all fields of the Teacher model