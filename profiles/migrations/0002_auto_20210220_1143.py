# Generated by Django 3.1.5 on 2021-02-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avail',
            name='canceledEmail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='avail',
            name='confirmedEmail',
            field=models.IntegerField(default=0),
        ),
    ]