# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('action_id', models.AutoField(db_column='action_id', primary_key=True, serialize=False, unique=True, verbose_name='\u64cd\u4f5cID')),
                ('action_name', models.CharField(db_column='action_name', max_length=32, verbose_name='\u64cd\u4f5c\u540d\u79f0')),
                ('pre_action_id', models.IntegerField(db_column='pre_action_id', verbose_name='\u9884\u64cd\u4f5cID')),
                ('action_status', models.BooleanField(db_column='action_status', default=False, verbose_name='\u64cd\u4f5c\u8fd0\u884c\u72b6\u6001')),
                ('action_type', models.CharField(db_column='action_type', max_length=32, verbose_name='\u64cd\u4f5c\u7c7b\u578b')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time', verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['action_id', 'element_id'],
                'db_table': 'rx_action',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.IntegerField(db_column='device_type', verbose_name='\u9a71\u52a8\u7c7b\u578b')),
                ('device_id', models.CharField(db_column='device_id', max_length=64, unique=True, verbose_name='\u9a71\u52a8ID')),
                ('device_name', models.CharField(db_column='device_name', max_length=32, verbose_name='\u9a71\u52a8\u540d\u79f0')),
                ('platform_version', models.CharField(db_column='platform_version', max_length=16, verbose_name='\u7cfb\u7edf\u7248\u672c')),
                ('app_package', models.CharField(db_column='app_package', max_length=64, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('app_activity', models.CharField(db_column='app_activity', max_length=64, verbose_name='\u5e94\u7528Activity')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'rx_device',
            },
        ),
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('element_id', models.AutoField(db_column='element_id', primary_key=True, serialize=False, unique=True, verbose_name='\u5143\u7d20\u7f16\u53f7')),
                ('element_name', models.CharField(db_column='element_name', max_length=32, verbose_name='\u5143\u7d20\u540d\u79f0')),
                ('element_value', models.CharField(db_column='element_value', max_length=255, verbose_name='\u5143\u7d20\u4f4d\u7f6e')),
                ('element_type', models.CharField(db_column='element_type', max_length=16, verbose_name='\u5143\u7d20\u5b9a\u4f4d\u7c7b\u578b')),
                ('group_type', models.BooleanField(db_column='group_type', default=True, verbose_name='\u5143\u7d20\u6570\u7ec4')),
                ('is_delete', models.BooleanField(db_column='is_delete', default=False, verbose_name='\u5220\u9664\u72b6\u6001')),
            ],
            options={
                'ordering': ['element_id'],
                'db_table': 'rx_elements',
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('interface_id', models.AutoField(db_column='interface_id', primary_key=True, serialize=False, unique=True, verbose_name='\u63a5\u53e3ID')),
                ('interface_name', models.CharField(db_column='interface_name', max_length=32, verbose_name='\u63a5\u53e3\u540d\u79f0')),
                ('interface_type', models.IntegerField(db_column='interface_type', default=0, verbose_name='\u63a5\u53e3\u7c7b\u578b')),
                ('request_type', models.IntegerField(db_column='request_type', default=0, verbose_name='\u8bf7\u6c42\u7c7b\u578b')),
                ('url', models.CharField(db_column='url', max_length=128, verbose_name='\u8bf7\u6c42\u5730\u5740')),
            ],
            options={
                'ordering': ['interface_name'],
                'db_table': 'rx_interface',
            },
        ),
        migrations.CreateModel(
            name='InterfaceCase',
            fields=[
                ('case_id', models.AutoField(db_column='case_id', primary_key=True, serialize=False, unique=True, verbose_name='\u63a5\u53e3\u7528\u4f8b\u7f16\u53f7')),
                ('case_name', models.CharField(db_column='case_name', max_length=32, verbose_name='\u63a5\u53e3\u7528\u4f8b\u540d\u79f0')),
                ('parameter', models.CharField(db_column='parameter', max_length=128, verbose_name='\u8bf7\u6c42\u53c2\u6570')),
                ('expect', models.CharField(db_column='expect', max_length=255, verbose_name='\u671f\u671b\u7ed3\u679c')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, db_column='update_time', verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('is_delete', models.BooleanField(db_column='is_delete', default=False, verbose_name='\u5220\u9664\u72b6\u6001')),
                ('interface_id', models.ForeignKey(db_column='interface_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Interface', verbose_name='\u5173\u8054\u63a5\u53e3ID')),
            ],
            options={
                'ordering': ['case_id'],
                'db_table': 'rx_interface_case',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.AutoField(db_column='module_id', primary_key=True, serialize=False, unique=True, verbose_name='\u6a21\u5757ID')),
                ('module_name', models.CharField(db_column='module_name', max_length=32, verbose_name='\u6a21\u5757\u540d\u79f0')),
                ('module_desc', models.CharField(db_column='module_desc', max_length=255, verbose_name='\u6a21\u5757\u63cf\u8ff0')),
            ],
            options={
                'ordering': ['module_id'],
                'db_table': 'rx_module',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(db_column='project_id', primary_key=True, serialize=False, unique=True, verbose_name='\u9879\u76eeID')),
                ('project_name', models.CharField(db_column='project_name', max_length=64, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('project_desc', models.CharField(db_column='project_desc', max_length=255, verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['project_id'],
                'db_table': 'rx_project',
            },
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('suite_id', models.AutoField(db_column='element_id', primary_key=True, serialize=False, unique=True, verbose_name='\u6d4b\u8bd5\u96c6\u7f16\u53f7')),
                ('suite_name', models.CharField(db_column='suite_name', max_length=32, verbose_name='\u6d4b\u8bd5\u96c6\u540d\u79f0')),
                ('project_id', models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Project', verbose_name='\u5173\u8054\u9879\u76ee')),
            ],
            options={
                'ordering': ['suite_id'],
                'db_table': 'rx_suite',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(db_column='user_id', primary_key=True, serialize=False, unique=True, verbose_name='\u7528\u6237ID')),
                ('user_name', models.CharField(db_column='user_name', max_length=32, verbose_name='\u7528\u6237\u540d')),
                ('gender', models.BooleanField(db_column='gender', default=True, verbose_name='\u6027\u522b')),
                ('email', models.CharField(db_column='email', max_length=32, verbose_name='\u90ae\u7bb1')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'ordering': ['user_id'],
                'db_table': 'rx_user',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.User', verbose_name='\u7528\u6237ID'),
        ),
        migrations.AddField(
            model_name='module',
            name='project_id',
            field=models.ForeignKey(db_column='project_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Project', verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='interfacecase',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.User', verbose_name='\u521b\u5efa\u4eba'),
        ),
        migrations.AddField(
            model_name='interface',
            name='module_id',
            field=models.ForeignKey(db_column='module_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Module', verbose_name='\u6a21\u5757ID'),
        ),
        migrations.AddField(
            model_name='elements',
            name='module_id',
            field=models.ForeignKey(db_column='module_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Module', verbose_name='\u5173\u8054\u6a21\u5757'),
        ),
        migrations.AddField(
            model_name='action',
            name='element_id',
            field=models.ForeignKey(db_column='element_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Elements', verbose_name='\u5173\u8054\u5143\u7d20'),
        ),
        migrations.AddField(
            model_name='action',
            name='module_id',
            field=models.ForeignKey(db_column='module_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Module', verbose_name='\u5173\u8054\u6a21\u5757'),
        ),
        migrations.AddField(
            model_name='action',
            name='suite_id',
            field=models.ForeignKey(db_column='suite_id', on_delete=django.db.models.deletion.CASCADE, to='RelaxMind.Suite', verbose_name='\u5173\u8054\u6d4b\u8bd5\u96c6'),
        ),
    ]
