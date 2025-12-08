from django.db import models
from django.core.validators import RegexValidator


# Teacher model representing school teachers
class Teacher(models.Model):
    GENDER_CHOICES =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]# Choices for gender field

    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='teacher_profile'
    )#Link Teacher to CustomUser model

    teacher_contact = models.CharField(max_length=15, 
                                      unique=True, 
                                      validators=[RegexValidator(r'^\+?\d{9,15}$')]) # Validates phone number format
    
    date_hired = models.DateField(auto_now_add=True)# Date when the teacher was hired
    subject_specialization = models.CharField(max_length=100)# Subject specialization of the teacher
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)# Gender of the teacher

    def __str__(self):
        return f"{self.username} ({self.role})"