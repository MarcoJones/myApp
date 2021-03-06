# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from models import Students


def index(request):
    # stu = Students.objects.values("sName", "sAge", "sGender", "sScore", "sGrade", "createTime", "isDelete")
    # Home page
    return render(request, "home.html")


def projects(request):
    # Project management page
    return render(request, "project.html")


def interface_case(request):
    # Interface case data list page
    return render(request, "interface_case.html")


def modules(request):
    # Modules management page
    return render(request, 'modules.html')


def driver(request):
    # Get ui elements driver page
    return render(request, 'driver.html')


def ui_element(request):
    #
    return render(request, 'ui_elements.html')


def user_manage(request):
    # User management page
    return render(request, 'user.html')


def project_ajax(request):
    project_name = request.POST.get('project_name')
    # project_desc = request.POST.get('project_desc')
    if project_name is None:
        return HttpResponse(False)
    else:
        return HttpResponse(True)



def test(request):
    return render(request, "test.html")