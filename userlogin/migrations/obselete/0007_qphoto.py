# Generated by Django 3.1.1 on 2020-11-22 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userlogin.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userlogin', '0006_auto_20201031_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to=userlogin.models.path_and_rename)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]