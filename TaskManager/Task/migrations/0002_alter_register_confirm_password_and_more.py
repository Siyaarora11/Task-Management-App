# Generated by Django 5.2 on 2025-04-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='confirm_password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(),
        ),
    ]
