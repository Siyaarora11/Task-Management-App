# Generated by Django 5.1.6 on 2025-04-25 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_addtask_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='deadline',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 5, 2, 14, 19, 9, 256328, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='register',
            name='confirm_password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
