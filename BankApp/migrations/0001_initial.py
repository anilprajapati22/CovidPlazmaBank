# Generated by Django 3.2.5 on 2021-07-31 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('BloodGrp', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('is_diabitic', models.BooleanField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('Rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('BloodGrp', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('is_diabitic', models.BooleanField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('Did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
