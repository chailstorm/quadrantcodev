# Generated by Django 3.1.1 on 2020-11-22 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0007_qphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='qphoto',
            name='pid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
