from django.urls import path, include
from .views import TeacherViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]