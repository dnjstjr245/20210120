# Generated by Django 3.1.5 on 2021-01-15 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='members',
            table='o2_users',
        ),
    ]
