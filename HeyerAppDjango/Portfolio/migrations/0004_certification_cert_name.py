# Generated by Django 4.1 on 2022-09-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_rename_portfolio_project_alter_education_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='cert_name',
            field=models.CharField(default='Proficiency Certificate', max_length=128, verbose_name='Certificate Name'),
        ),
    ]
