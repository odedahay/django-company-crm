# Generated by Django 2.2 on 2020-02-29 12:29

from django.db import migrations, models
import reports.models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_problemreported_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemreported',
            name='problem_id',
            field=models.CharField(blank=True, default=reports.models.random_code, max_length=12, unique=True),
        ),
    ]
