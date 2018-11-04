# Generated by Django 2.1.2 on 2018-11-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient_db',
            name='Maritial_Status',
        ),
        migrations.AddField(
            model_name='patient_db',
            name='medical_con',
            field=models.CharField(default='No Problems', max_length=255),
        ),
        migrations.AlterField(
            model_name='patient_db',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient_db',
            name='Emergency_num',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='patient_db',
            name='Phone_num',
            field=models.CharField(max_length=13),
        ),
    ]