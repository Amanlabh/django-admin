# assignment/models.py
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TeacherStudent(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'student')

class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certificate_pdf = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"Certificate for {self.student.name} by {self.teacher.name}"
