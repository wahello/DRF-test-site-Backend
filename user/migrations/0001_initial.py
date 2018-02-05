# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('username_slug', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False, verbose_name='activation')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]