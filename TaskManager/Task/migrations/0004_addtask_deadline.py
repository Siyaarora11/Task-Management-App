# Generated by Django 5.2 on 2025-04-25 10:10

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_addtask'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2025, 5, 2, 10, 9, 58, 845724, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
