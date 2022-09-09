# Generated by Django 4.1 on 2022-09-09 06:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certifier', models.CharField(max_length=128, verbose_name='Certifier')),
                ('year_attained', models.DateField(default=django.utils.timezone.now, verbose_name='Year Attained')),
                ('link', models.URLField(default='https://heyer.app', max_length=128, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Certification',
                'verbose_name_plural': 'Certifications',
                'ordering': ['-year_attained'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=128, verbose_name='Institute')),
                ('start_year', models.CharField(max_length=4, verbose_name='Start Year')),
                ('end_year', models.CharField(default='now', max_length=4, verbose_name='End Year')),
                ('link', models.URLField(default='https://heyer.app', max_length=128, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Education',
                'ordering': ['-start_year'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=128, verbose_name='Company')),
                ('start_year', models.CharField(max_length=4, verbose_name='Start Year')),
                ('end_year', models.CharField(default='now', max_length=4, verbose_name='End Year')),
                ('link', models.URLField(default='https://heyer.app', max_length=128, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Experience',
                'ordering': ['-start_year'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('year_created', models.DateField(default=django.utils.timezone.now, verbose_name='Year Created')),
                ('link', models.URLField(default='https://heyer.app', max_length=128, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio Projects',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('years', models.IntegerField(verbose_name='Years')),
                ('link', models.URLField(default='https://heyer.app', max_length=128, verbose_name='Link')),
                ('image', models.URLField(default='https://via.placeholder.com/60C/O', max_length=128, verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ['name'],
            },
        ),
    ]
