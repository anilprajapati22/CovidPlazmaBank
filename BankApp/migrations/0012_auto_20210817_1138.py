# Generated by Django 3.2.5 on 2021-08-17 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BankApp', '0011_auto_20210817_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donnermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='donnermodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='requestermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='requestermodel',
            name='state',
        ),
    ]
