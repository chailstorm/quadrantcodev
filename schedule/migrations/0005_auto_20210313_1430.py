# Generated by Django 3.1.5 on 2021-03-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_auto_20210313_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forwards',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
