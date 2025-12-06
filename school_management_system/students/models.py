from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
    user = models.OneToOneField(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    date_of_birth = models.DateField()
    mother_full_name = models.CharField(max_length=200)
    father_full_name = models.CharField(max_length=200)
    parent_contact = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^\+?\d{9,15}$')])
    home_address = models.TextField()
    medical_allergies = models.TextField()
    
    


