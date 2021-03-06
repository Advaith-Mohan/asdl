# Generated by Django 2.1.5 on 2020-12-22 18:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20201222_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
                ('room_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.roomInfo')),
            ],
        ),
        migrations.AlterField(
            model_name='lab',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 0, 22, 14, 200705)),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='date_of_admn',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 0, 22, 14, 201698)),
        ),
    ]
