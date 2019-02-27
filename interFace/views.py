# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import Students


def index(request):
    stu = Students.objects.values("sName", "sAge", "sGender", "sScore", "sGrade", "createTime", "isDelete")
    return render(request, "home.html", {'stu': stu})
