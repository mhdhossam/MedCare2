# Generated by Django 4.1.3 on 2022-11-28 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pactientaccount',
            name='gender',
        ),
    ]
