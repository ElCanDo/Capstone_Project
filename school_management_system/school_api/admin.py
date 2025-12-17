from django.contrib import admin
from .models import Classroom, Teacher, Student, Enrollment, TeacherAssign

admin.site.register(Classroom)
admin.site.register(Teacher)
admin.site.register(Student)
class EnrollmentAdmin(admin.ModelAdmin):
    model = Enrollment
    list_display = ('student', 'classroom', 'date_enrolled')

admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(TeacherAssign)    