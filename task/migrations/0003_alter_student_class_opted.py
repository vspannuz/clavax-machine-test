# Generated by Django 3.2.7 on 2021-10-17 01:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_rename_phone_no_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_opted',
            field=models.IntegerField(max_length=2, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
