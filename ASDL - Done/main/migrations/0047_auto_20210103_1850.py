# Generated by Django 2.1.5 on 2021-01-03 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20210103_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 3, 18, 50, 14, 283194)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 3, 18, 50, 14, 283194)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_dis',
            field=models.DateTimeField(null=True),
        ),
    ]