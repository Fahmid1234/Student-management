# Generated by Django 5.0.7 on 2024-08-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_transport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='time',
            field=models.TimeField(),
        ),
    ]
