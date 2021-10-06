# Generated by Django 2.1.5 on 2020-12-21 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201220_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roominfo',
            name='status',
        ),
        migrations.AddField(
            model_name='roominfo',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 21, 14, 10, 306338)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 21, 21, 14, 10, 306338)),
        ),
    ]
