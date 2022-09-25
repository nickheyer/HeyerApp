# Generated by Django 4.1 on 2022-09-25 01:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0004_certification_cert_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certification',
            options={'ordering': ['-date_attained'], 'verbose_name': 'Certification', 'verbose_name_plural': 'Certifications'},
        ),
        migrations.RemoveField(
            model_name='certification',
            name='year_attained',
        ),
        migrations.AddField(
            model_name='certification',
            name='date_attained',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date Attained'),
        ),
    ]
