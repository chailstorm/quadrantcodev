# Generated by Django 3.1.1 on 2020-11-22 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0010_qinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qinfo',
            name='user',
        ),
    ]
