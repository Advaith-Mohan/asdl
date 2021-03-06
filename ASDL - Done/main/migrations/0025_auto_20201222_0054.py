# Generated by Django 2.1.5 on 2020-12-21 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20201222_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 0, 54, 11, 519914)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 0, 54, 11, 519914)),
        ),
        migrations.AlterField(
            model_name='roominfo',
            name='room_type',
            field=models.CharField(choices=[('S', 'SINGLE'), ('D', 'DOUBLE'), ('S/AC', 'SINGLE(AC)'), ('D/AC', 'DOUBLE(AC)')], max_length=10),
        ),
    ]
