# Generated by Django 2.1.3 on 2018-12-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0010_auto_20181208_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='d_website',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
