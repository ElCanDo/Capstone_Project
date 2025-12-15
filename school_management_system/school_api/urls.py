from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (CustomUserViewSet, 
                    ClassroomViewSet, 
                    TeacherViewSet, 
                    StudentViewSet, 
                    EnrollmentViewSet,
                    TeacherAssignViewSet)

router = DefaultRouter() 
router.register(r'users', CustomUserViewSet)
router.register('classrooms', ClassroomViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)
router.register('enrollments', EnrollmentViewSet)
router.register('teacher_assignment', TeacherAssignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]