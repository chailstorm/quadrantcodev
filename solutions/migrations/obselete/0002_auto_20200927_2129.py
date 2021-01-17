# Generated by Django 3.1.1 on 2020-09-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qinfo',
            name='capitalplan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='dataanalysis',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='leadingmeetings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='operationsfinance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='personalitytypes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='personalleadership',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='processimprove',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='productivity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='pysicianrecruitment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='servicelinedev',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='teamcourses',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='tempassignments',
            field=models.IntegerField(default=0),
        ),
    ]