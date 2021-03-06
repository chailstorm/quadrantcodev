# Generated by Django 3.1.1 on 2020-11-22 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0007_auto_20201115_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qinfo',
            name='capitalplan',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='dataanalysis',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='leadingmeetings',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='operationsfinance',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='personalitytypes',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='personalleadership',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='processimprove',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='productivity',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='pysicianrecruitment',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='servicelinedev',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='teamcourses',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='tempassignments',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=0),
        ),
    ]
