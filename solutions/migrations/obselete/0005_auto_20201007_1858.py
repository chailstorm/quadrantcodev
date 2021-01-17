# Generated by Django 3.1.1 on 2020-10-07 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0004_qinfo_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='qinfo',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='qinfo',
            name='active',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=1),
        ),
    ]
