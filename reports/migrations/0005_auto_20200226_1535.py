# Generated by Django 2.2 on 2020-02-26 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20200225_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-created',)},
        ),
    ]
