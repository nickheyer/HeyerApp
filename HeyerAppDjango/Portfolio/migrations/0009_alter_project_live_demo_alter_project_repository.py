# Generated by Django 4.1 on 2022-09-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0008_project_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_demo',
            field=models.URLField(default=None, max_length=256, null=True, verbose_name='Live Demo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='repository',
            field=models.URLField(default=None, max_length=256, null=True, verbose_name='Repository'),
        ),
    ]
