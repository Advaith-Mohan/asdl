# Generated by Django 2.1.5 on 2020-12-23 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20201223_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='name',
            field=models.CharField(default='NONAME', max_length=20),
        ),
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 20, 1, 48, 752530)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 20, 1, 48, 752530)),
        ),
    ]