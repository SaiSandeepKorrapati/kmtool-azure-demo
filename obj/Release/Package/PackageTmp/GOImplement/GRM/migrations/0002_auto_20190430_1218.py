# Generated by Django 2.1.4 on 2019-04-30 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GRM', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='hexRegion',
            new_name='Region',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='status',
        ),
        migrations.RemoveField(
            model_name='resourceprojects',
            name='end',
        ),
        migrations.RemoveField(
            model_name='resourceprojects',
            name='start',
        ),
        migrations.RemoveField(
            model_name='resources',
            name='location',
        ),
        migrations.RemoveField(
            model_name='resourcetrainings',
            name='end',
        ),
        migrations.RemoveField(
            model_name='resourcetrainings',
            name='start',
        ),
        migrations.AddField(
            model_name='resourceprojects',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourceprojects',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourcetrainings',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resourcetrainings',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productskills',
            name='productSkill',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='GRM.Disciplines'),
        ),
    ]
