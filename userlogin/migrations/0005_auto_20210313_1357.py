# Generated by Django 3.1.5 on 2021-03-13 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0004_passwordreset_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordreset',
            old_name='link',
            new_name='url',
        ),
    ]
