# Generated by Django 5.0.7 on 2024-08-07 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_attendance_subject_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
        ),
    ]
