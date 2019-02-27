# -*- coding: utf-8 -*-

from django.http import HttpResponse
from interFace.models import Grades
from interFace.models import Students
import django


# def add_grade(request):
#     grade = Grades(gradeName='3', studentNum='50', girlNum='25', boyNum='25', isDelete='False')
#     grade.save()
#     return HttpResponse("<p>添加班级数据成功！</p>")


def add_student(request):
    student = Students(sName='Lee', sAge='27', sGender=False, sScore='99', isDelete=False, sGrade=Grades.objects.get(id='2'))
    student.save()
    return HttpResponse("<p>添加班级数据成功！</p>")

if __name__ == '__main__':
    add_student()