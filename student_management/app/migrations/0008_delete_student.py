# Generated by Django 5.0.3 on 2024-04-05 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_student_course_id_remove_student_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]