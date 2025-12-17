from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
       
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    
""" Classroom model """

class Classroom(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name 
 
    
"""Teacher Model Definition"""

class Teacher(models.Model):
   
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='teacher_profile'
    )
    full_name = models.CharField(max_length=100, null=False, blank=False, default="Unknown teacher")
    teacher_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) 
    subject_specialization = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_employed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.user.role}"
      

"""Student Model"""

class Student(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    
    full_name = models.CharField(max_length=100, null=False, blank=False, default="Unknown Student")

    date_of_birth = models.DateField()

    mother_full_name = models.CharField(max_length=100)
    
    mother_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) 
    
    father_full_name = models.CharField(max_length=100)

    father_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')] 
        )
    home_address = models.TextField(blank=True, null=True)

    medical_allergies = models.TextField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    enrollment_date = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return f"{self.full_name} - {self.user.role}"
    

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'classroom')
    
    def __str__(self):
        return f"{self.student.full_name} is enrolled into: {self.classroom.name}"


class TeacherAssign(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'classroom')

    def __str__(self):
        return f"{self.teacher.full_name} is assigned to : {self.classroom.name}"