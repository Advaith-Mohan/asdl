# Generated by Django 2.1.5 on 2020-12-23 14:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20201223_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 19, 57, 2, 819662)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roomInfo'),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 19, 57, 2, 819662)),
        ),
    ]