# Generated by Django 2.1.5 on 2020-12-21 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20201222_0014'),
    ]

    operations = [
        migrations.DeleteModel(
            name='roomNew',
        ),
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 0, 49, 18, 553534)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 0, 49, 18, 554492)),
        ),
    ]
