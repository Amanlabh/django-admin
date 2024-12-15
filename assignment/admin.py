# assignment/admin.py
from django.contrib import admin
from .models import Teacher, Student, TeacherStudent, Certificate

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(TeacherStudent)
admin.site.register(Certificate)
