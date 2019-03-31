# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
# from models import Students


def index(request):
    # stu = Students.objects.values("sName", "sAge", "sGender", "sScore", "sGrade", "createTime", "isDelete")
    return render(request, "home.html")


def projects(request):
    return render(request, "project.html")


def interface_case(request):
    return render(request, "interface_case.html")


def modules(request):
    return render(request, 'modules.html')


def driver(request):
    return render(request, 'driver.html')


def ui_element(request):
    return render(request, 'ui_elements.html')

def user_manage(request):
    return render(request, 'user.html')
