# Generated by Django 2.1.5 on 2021-01-15 14:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_auto_20210115_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 19, 49, 44, 571353)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 19, 49, 44, 572349)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_dis',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 19, 49, 44, 572349), null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roomInfo'),
        ),
    ]
