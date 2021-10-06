# Generated by Django 2.1.5 on 2020-12-23 14:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20201223_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 19, 45, 30, 211385)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 19, 45, 30, 211385)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roomInfo'),
        ),
    ]
