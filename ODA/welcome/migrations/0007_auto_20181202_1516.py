# Generated by Django 2.1.3 on 2018-12-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_auto_20181127_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_db',
            name='Blood_group',
            field=models.CharField(max_length=5),
        ),
    ]