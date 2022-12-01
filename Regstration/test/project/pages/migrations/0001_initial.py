# Generated by Django 4.1.3 on 2022-11-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pactientaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('mobilenumber', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
                ('NationalId', models.IntegerField()),
            ],
        ),
    ]
