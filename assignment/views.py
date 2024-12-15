# assignment/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Teacher, Student, Certificate
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import jwt
from datetime import datetime, timedelta
from django.conf import settings


# Level 1: Display lists of teachers and students
def teacher_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def student_view(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def get_students_for_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    students = teacher.student_set.all()
    return render(request, 'student_list.html', {'students': students})

def get_teachers_for_student(request, student_id):
    student = Student.objects.get(id=student_id)
    teachers = student.teacher_set.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})


# Level 2: Generate a certificate for teacher-student pair
def generate_certificate(request, teacher_id, student_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    student = get_object_or_404(Student, id=student_id)

    # Create PDF Response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{teacher.name}_{student.name}.pdf"'

    # Create a PDF using reportlab
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Certificate of Completion")
    p.drawString(100, 730, f"This certifies that {student.name}")
    p.drawString(100, 710, f"has successfully completed the course under {teacher.name}")
    p.showPage()
    p.save()

    # Optional: Store the certificate in the database (if desired)
    certificate = Certificate.objects.create(
        teacher=teacher,
        student=student,
        certificate_pdf=response
    )

    return response


# Level 3: Verify certificate using JWT token
def generate_jwt(teacher_id, student_id):
    # Secret key for encoding JWT
    secret_key = settings.SECRET_KEY
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    payload = {
        'teacher_id': teacher_id,
        'student_id': student_id,
        'exp': expiration_time
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def verify_certificate(request, token):
    try:
        secret_key = settings.SECRET_KEY
        decoded_data = jwt.decode(token, secret_key, algorithms=['HS256'])

        teacher_id = decoded_data['teacher_id']
        student_id = decoded_data['student_id']

        teacher = get_object_or_404(Teacher, id=teacher_id)
        student = get_object_or_404(Student, id=student_id)

        return HttpResponse(f"Certificate verified: {teacher.name} taught {student.name}")
    except jwt.ExpiredSignatureError:
        return HttpResponse("Token expired", status=400)
    except jwt.InvalidTokenError:
        return HttpResponse("Invalid token", status=400)
