# Generated by Django 3.1.1 on 2020-12-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qinfo',
            fields=[
                ('qn', models.IntegerField(primary_key=True, serialize=False)),
                ('active', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=1)),
                ('prefix', models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Dr.', 'Dr.')], max_length=255)),
                ('first', models.CharField(max_length=255)),
                ('last', models.CharField(max_length=255)),
                ('suffix', models.CharField(blank=True, choices=[('PhD', 'PhD'), ('M.D.', 'M.D.')], max_length=255)),
                ('category', models.CharField(choices=[('medicine', 'Medicine')], max_length=255)),
                ('servicelinedev', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('capitalplan', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('pysicianrecruitment', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('processimprove', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('productivity', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('operationsfinance', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('leadingmeetings', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('dataanalysis', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('teamcourses', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('personalleadership', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('personalitytypes', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('tempassignments', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('special1', models.CharField(max_length=255)),
                ('special2', models.CharField(max_length=255)),
                ('special3', models.CharField(max_length=255)),
                ('special4', models.CharField(max_length=255)),
                ('special5', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('linkedin', models.TextField(blank=True)),
                ('yearexp', models.IntegerField()),
                ('email', models.CharField(default='example@gmail.com', max_length=255)),
                ('cost', models.IntegerField(default=100)),
            ],
        ),
    ]
