# Generated by Django 3.1.1 on 2020-09-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_auto_20200927_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qinfo',
            name='linkedin',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special5',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
