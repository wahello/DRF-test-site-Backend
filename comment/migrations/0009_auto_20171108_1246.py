# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_articlecomment_answer_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='answer_target',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_comment', to='comment.ArticleComment'),
        ),
    ]