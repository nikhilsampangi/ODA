# Generated by Django 2.1.2 on 2018-11-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='latlng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Age', models.CharField(max_length=3)),
                ('Gender', models.CharField(max_length=10)),
                ('Blood_group', models.CharField(max_length=3)),
                ('Maritial_Status', models.CharField(max_length=3)),
                ('Phone_num', models.CharField(max_length=12)),
                ('Emergency_num', models.CharField(max_length=12)),
                ('PatientId', models.CharField(default='0', max_length=255)),
                ('Email_Id', models.CharField(default='NULL', max_length=255)),
            ],
        ),
    ]