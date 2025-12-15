from django.shortcuts import render
from rest_framework import viewsets, permissions,authentication
from . serializers import (CustomUserSerializer, 
                           ClassroomSerializer, 
                           TeacherSerializer, 
                           StudentSerializer, 
                           EnrollmentSerializer, 
                           TeacherAssignSerializer)
from .models import CustomUser, Classroom, Teacher, Student, Enrollment, TeacherAssign

"""Viewsets For all the Models"""

class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializer()

class ClassroomViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Teacher.objects.all() 
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class TeacherAssignViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    queryset = TeacherAssign.objects.all()
    serializer_class = TeacherAssignSerializer