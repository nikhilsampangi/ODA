# Generated by Django 2.1.3 on 2018-12-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_auto_20181202_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_db',
            name='Emergency_num',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
