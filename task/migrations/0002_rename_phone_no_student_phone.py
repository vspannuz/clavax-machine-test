# Generated by Django 3.2.1 on 2021-10-14 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone_no',
            new_name='phone',
        ),
    ]
