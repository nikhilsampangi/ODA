# Generated by Django 2.1.2 on 2018-12-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0018_auto_20181210_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='Latitudes',
            field=models.CharField(blank=True, default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Longitudes',
            field=models.CharField(blank=True, default=0, max_length=30),
        ),
    ]