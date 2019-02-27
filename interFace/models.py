# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Grades(models.Model):
    gradeName  = models.CharField(max_length=50, db_column="grade_name", unique=True)
    studentNum = models.IntegerField(db_column="student_num")
    girlNum   = models.IntegerField(db_column="girls_num")
    boyNum   = models.IntegerField(db_column="boy_num")
    createTime = models.DateTimeField(auto_now_add=True, db_column="create_time")
    isDelete   = models.BooleanField(default=False)

    def __unicode__(self):
        return self.gradeName

    class Meta:
        db_table = "grades"
        ordering = ["id"]


class Students(models.Model):
    sName      = models.CharField(max_length=20, db_column="student_name")
    sAge       = models.IntegerField(db_column="age")
    sGender    = models.BooleanField(default=True, db_column="gender")
    sScore     = models.IntegerField(db_column="score")
    createTime = models.DateTimeField(auto_now_add=True)
    isDelete   = models.BooleanField(default=False)
    sGrade     = models.ForeignKey("Grades", db_column='grade')

    def __unicode__(self):
        return self.sName

    class Meta:
        db_table = "students"
        ordering = ["id"]