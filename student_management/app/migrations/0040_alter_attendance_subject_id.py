# Generated by Django 5.0.7 on 2024-08-07 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_attendance_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='subject_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.subject'),
        ),
    ]
