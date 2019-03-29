# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myApp.settings")
# django.setup()


# class Grades(models.Model):
#     gradeName  = models.CharField(max_length=50, db_column="grade_name", unique=True)
#     studentNum = models.IntegerField(db_column="student_num")
#     girlNum   = models.IntegerField(db_column="girls_num")
#     boyNum   = models.IntegerField(db_column="boy_num")
#     createTime = models.DateTimeField(auto_now_add=True, db_column="create_time")
#     isDelete   = models.BooleanField(default=False)
#
#     def __unicode__(self):
#         return self.gradeName
#
#     class Meta:
#         db_table = "grades"
#         ordering = ["id"]
#
#
# class Students(models.Model):
#     sName      = models.CharField(max_length=20, db_column="student_name")
#     sAge       = models.IntegerField(db_column="age")
#     sGender    = models.BooleanField(default=True, db_column="gender")
#     sScore     = models.IntegerField(db_column="score")
#     createTime = models.DateTimeField(auto_now_add=True)
#     isDelete   = models.BooleanField(default=False)
#     sGrade     = models.ForeignKey("Grades", db_column='grade')
#
#     def __unicode__(self):
#         return self.sName
#
#     class Meta:
#         db_table = "students"
#         ordering = ["id"]


class User(models.Model):
    """
    User table for manage test project and use
    gender: True---Male, False---Female
    """
    user_id = models.AutoField(primary_key=True, db_column='user_id', unique=True, verbose_name=u'用户ID')
    user_name = models.CharField(max_length=32, db_column='user_name', verbose_name=u'用户名')
    gender = models.BooleanField(default=True, db_column='gender', verbose_name=u'性别')
    email = models.CharField(max_length=32, db_column='email', verbose_name=u'邮箱')
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name=u'创建时间')

    def __unicode__(self):
        return self.user_name

    class Meta:
        db_table = 'rx_user'
        ordering = ['user_id']


class Project(models.Model):
    """
    Test project table,For manage
    """
    project_id = models.AutoField(primary_key=True, db_column='project_id', unique=True, verbose_name=u'项目ID')
    project_name = models.CharField(max_length=64, db_column='project_name', verbose_name=u'项目名称')
    project_desc = models.CharField(max_length=255, db_column='project_desc', verbose_name=u'项目描述')
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name=u'创建时间')
    user_id = models.ForeignKey('User', db_column='user_id', verbose_name=u'用户ID')

    def __unicode__(self):
        return self.project_name

    class Meta:
        db_table = 'rx_project'
        ordering = ['project_id']


class Module(models.Model):
    """
    Function module from project
    """
    module_id = models.AutoField(primary_key=True, db_column='module_id', unique=True, verbose_name=u'模块ID')
    module_name = models.CharField(max_length=32, db_column='module_name', verbose_name=u'模块名称')
    module_desc = models.CharField(max_length=255, db_column='module_desc', verbose_name=u'模块描述')
    project_id = models.ForeignKey('Project', db_column='project_id', verbose_name=u'项目名称')

    def __unicode__(self):
        return self.module_name

    class Meta:
        db_table = 'rx_module'
        ordering = ['module_id']


class Interface(models.Model):
    """
    interface_type: 0---HTTP, 1---TCP;
    request_type: 0---Get, 1---Post
    """
    interface_id = models.AutoField(primary_key=True, db_column='interface_id', unique=True, verbose_name=u'接口ID')
    interface_name = models.CharField(max_length=32, db_column='interface_name', verbose_name=u'接口名称')
    module_id = models.ForeignKey('Module', db_column='module_id', verbose_name=u'模块ID')
    interface_type = models.IntegerField(default=0, db_column='interface_type', verbose_name=u'接口类型')
    request_type = models.IntegerField(default=0, db_column='request_type', verbose_name=u'请求类型')
    url = models.CharField(max_length=128, db_column='url', verbose_name=u'请求地址')

    def __unicode__(self):
        return self.case_name

    class Meta:
        db_table = 'rx_interface'
        ordering = ['interface_name']


class InterfaceCase(models.Model):
    """
    Interface test case table
    is_delete：False---UnDelete, True---Deleted
    """
    case_id = models.AutoField(primary_key=True, db_column='case_id', unique=True, verbose_name=u'接口用例编号')
    case_name = models.CharField(max_length=32, db_column='case_name', verbose_name=u'接口用例名称')
    interface_id = models.ForeignKey('Interface', db_column='interface_id', verbose_name=u'关联接口ID')
    parameter = models.CharField(max_length=128, db_column='parameter', verbose_name=u'请求参数')
    expect = models.CharField(max_length=255, db_column='expect', verbose_name=u'期望结果')
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, db_column='update_time', verbose_name=u'更新时间')
    is_delete = models.BooleanField(default=False, db_column='is_delete', verbose_name='删除状态')
    user_id = models.ForeignKey('User', db_column='user_id', verbose_name=u'创建人')

    def __unicode__(self):
        return self.case_name

    class Meta:
        db_table = 'rx_interface_case'
        ordering = ['case_id']


class Devices(models.Model):
    """
    Save android/iOS devices and Web browser config data
    device_type: 0---Android; 1---iOS; 2---Web
    device_id：Android/iOS----like:'FDGNW17213002562';Web---None
    device_name：Android---Sumsung Galaxy7/HonorV20...;iOS---iPhone5/6/7/8/XR...;Web---FireFox/IE/Google/360...
    platform_version：Android---4.4-9.0; iOS---7-12; Web---WindowsXP/7/8/10
    """
    device_type = models.IntegerField(db_column='device_type', verbose_name=u'驱动类型')
    device_id = models.CharField(max_length=64, db_column='device_id', unique=True, verbose_name=u'驱动ID')
    device_name = models.CharField(max_length=32, db_column='device_name', verbose_name=u'驱动名称')
    platform_version = models.CharField(max_length=16, db_column='platform_version', verbose_name=u'系统版本')
    app_package = models.CharField(max_length=64, db_column='app_package', verbose_name=u'应用名称')
    app_activity = models.CharField(max_length=64, db_column='app_activity', verbose_name=u'应用Activity')

    def __unicode__(self):
        return self.device_name

    class Meta:
        db_table = 'rx_device'
        ordering = ['id']


class Elements(models.Model):
    """
    Table save data for android/iOS/Web page elements
    element_type：id/class/name/xpath...
    group_type：True---single, False---batch
    is_delete：false---UnDelete, true---deleted
    """
    element_id = models.AutoField(primary_key=True, db_column='element_id', unique=True, verbose_name=u'元素编号')
    element_name = models.CharField(max_length=32, db_column='element_name', verbose_name=u'元素名称')
    element_value = models.CharField(max_length=255, db_column='element_value', verbose_name=u'元素位置')
    element_type = models.CharField(max_length=16, db_column='element_type', verbose_name='元素定位类型')
    group_type = models.BooleanField(default=True, db_column='group_type', verbose_name=u'元素数组')
    is_delete = models.BooleanField(default=False, db_column='is_delete', verbose_name=u'删除状态')
    module_id = models.ForeignKey('Module', db_column='module_id', verbose_name=u'关联模块')

    def __unicode__(self):
        return self.element_name

    class Meta:
        db_table = 'rx_elements'
        ordering = ['element_id']


class Suite(models.Model):
    """
    Test Suite contact actions
    """
    suite_id = models.AutoField(primary_key=True, db_column='element_id', unique=True, verbose_name=u'测试集编号')
    suite_name = models.CharField(max_length=32, db_column='suite_name', verbose_name=u'测试集名称')
    project_id = models.ForeignKey('Project', db_column='project_id', verbose_name=u'关联项目')

    def __unicode__(self):
        return self.suite_name

    class Meta:
        db_table = 'rx_suite'
        ordering = ['suite_id']


class Action(models.Model):
    """
    Element actions
    pre_action_id: Contact previous step execute status
    action_status：False---UnExecute; True---Executed
    action_type：like---click/send keys...
    """
    action_id = models.AutoField(primary_key=True, db_column='action_id', unique=True, verbose_name=u'操作ID')
    action_name = models.CharField(max_length=32, db_column='action_name', verbose_name=u'操作名称')
    element_id = models.ForeignKey('Elements', db_column='element_id', verbose_name=u'关联元素')
    module_id = models.ForeignKey('Module', db_column='module_id', verbose_name=u'关联模块')
    suite_id = models.ForeignKey('Suite', db_column='suite_id', verbose_name=u'关联测试集')
    pre_action_id = models.IntegerField(db_column='pre_action_id', verbose_name='预操作ID')
    action_status = models.BooleanField(default=False, db_column='action_status', verbose_name='操作运行状态')
    action_type = models.CharField(max_length=32, db_column='action_type', verbose_name=u'操作类型')
    create_time = models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, db_column='update_time', verbose_name=u'更新时间')

    def __unicode__(self):
        return self.action_name

    class Meta:
        db_table = 'rx_action'
        ordering = ['action_id', 'element_id']



