# Generated by Django 2.1.5 on 2020-12-10 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201210_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 20, 4, 30, 739783)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 10, 20, 4, 30, 740780)),
        ),
    ]
