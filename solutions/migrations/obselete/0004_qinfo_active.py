# Generated by Django 3.1.1 on 2020-10-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_auto_20200927_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='qinfo',
            name='active',
            field=models.IntegerField(choices=[(1, 1), (0, 0)], default=1),
            preserve_default=False,
        ),
    ]
