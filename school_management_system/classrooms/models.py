from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='classrooms')
    
    def __str__(self):
        return f"{self.name} - {self.grade.name}"    
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='subjects')
    
    def __str__(self):
        return f"{self.name} - {self.classroom.name}"    