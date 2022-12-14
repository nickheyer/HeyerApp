# Generated by Django 4.1 on 2022-09-25 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0012_alter_skill_options_remove_project_languages_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certification',
            options={'ordering': ['-pk'], 'verbose_name': 'Certification', 'verbose_name_plural': 'Certifications'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-pk'], 'verbose_name': 'Experience', 'verbose_name_plural': 'Experience'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['year_created'], 'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
