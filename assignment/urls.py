# assignment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teacher_view, name='teacher_list'),
    path('students/', views.student_view, name='student_list'),
    path('teacher/<int:teacher_id>/students/', views.get_students_for_teacher, name='students_for_teacher'),
    path('student/<int:student_id>/teachers/', views.get_teachers_for_student, name='teachers_for_student'),
    
    path('generate_certificate/<int:teacher_id>/<int:student_id>/', views.generate_certificate, name='generate_certificate'),
    path('verify_certificate/<str:token>/', views.verify_certificate, name='verify_certificate'),
]

