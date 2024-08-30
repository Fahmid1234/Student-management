# Generated by Django 5.0.7 on 2024-08-07 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_subject_course_alter_subject_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.staff'),
        ),
    ]
