# Generated by Django 3.2.5 on 2021-08-17 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BankApp', '0010_rename_bstate_banks_bstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donnermodel',
            name='donnate_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donnermodel',
            name='is_recived_by_bank',
            field=models.BooleanField(default=False),
        ),
    ]
