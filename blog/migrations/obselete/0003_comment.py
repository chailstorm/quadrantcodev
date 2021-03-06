# Generated by Django 3.1.1 on 2020-12-22 16:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201206_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('bcn', models.AutoField(primary_key=True, serialize=False)),
                ('bn', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Published'), (0, 'Hidden')])),
                ('author', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
