# Generated by Django 2.1.5 on 2021-01-15 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_auto_20210115_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 21, 41, 54, 947095)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 15, 21, 41, 54, 948093)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_dis',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
