# Generated by Django 2.1.3 on 2018-12-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0012_doctors_about_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='Other_info',
            field=models.TextField(blank=True, default='Its great', max_length=300),
        ),
    ]
