# Generated by Django 2.1.4 on 2019-05-02 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GRM', '0009_auto_20190502_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='projectManager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='GRM.Resources'),
        ),
    ]
