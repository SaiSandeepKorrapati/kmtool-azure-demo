# Generated by Django 2.1.4 on 2019-05-01 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRM', '0007_auto_20190430_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='createdDate',
            field=models.DateField(default=datetime.date(2019, 5, 1)),
        ),
    ]
