# Generated by Django 2.1.5 on 2020-12-23 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20201223_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 20, 7, 58, 14248)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 20, 7, 58, 14248)),
        ),
        migrations.AlterField(
            model_name='roominfo',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]
