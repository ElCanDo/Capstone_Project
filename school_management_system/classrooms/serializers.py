from rest_framework import serializers
from .models import Classroom, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'classroom']

    def validate(self, request):
        if Subject.objects.filter(
            name=data['name'],
            classroom=data['classroom']
        ).exists():
            raise serializers.ValidationError(
                "This subject exits already for this classroom."
                )
        return data

class ClassroomSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'grade', 'subject']


