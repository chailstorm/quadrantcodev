# Generated by Django 3.1.5 on 2021-03-13 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0007_passwordreset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='url',
            field=models.CharField(max_length=255),
        ),
    ]
