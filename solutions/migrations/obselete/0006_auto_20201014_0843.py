# Generated by Django 3.1.1 on 2020-10-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0005_auto_20201007_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qinfo',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special3',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special4',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='special5',
            field=models.CharField(max_length=255),
        ),
    ]