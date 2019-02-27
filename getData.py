# -*- coding: utf-8 -*-
from django.http import HttpResponse
from interFace.models import Grades
from interFace.models import Students


# def get_grade(request):
#     grade = Grades.objects.all()
#     return HttpResponse(grade)


def get_student(request):
    student = Students.objects.all()
    return HttpResponse(student)

if __name__ == '__main__':
    get_student()