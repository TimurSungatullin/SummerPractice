# Generated by Django 2.2.3 on 2020-05-12 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0002_auto_20200510_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamificationdiaryday',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 12, 22, 22, 0, 274049)),
        ),
        migrations.AlterField(
            model_name='gamificationpractice',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2020, 5, 12, 22, 22, 0, 297784)),
        ),
        migrations.AlterField(
            model_name='gamificationpractice',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2020, 5, 12, 22, 22, 0, 297764)),
        ),
    ]
