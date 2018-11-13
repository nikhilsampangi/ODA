# Generated by Django 2.1.2 on 2018-11-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181112_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_avail',
            name='BB_id',
        ),
        migrations.RemoveField(
            model_name='doctor_details',
            name='D_Id',
        ),
        migrations.DeleteModel(
            name='General_Medicine',
        ),
        migrations.RemoveField(
            model_name='stock_availability',
            name='shop_id',
        ),
        migrations.AddField(
            model_name='doctors',
            name='Degrees',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='doctors',
            name='Desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='Latitudes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='doctors',
            name='Longitudes',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='doctors',
            name='Phone',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Avail',
            field=models.BooleanField(blank=True),
        ),
        migrations.DeleteModel(
            name='Blood_avail',
        ),
        migrations.DeleteModel(
            name='Blood_Bank',
        ),
        migrations.DeleteModel(
            name='Doctor_Details',
        ),
        migrations.DeleteModel(
            name='Medical_shop',
        ),
        migrations.DeleteModel(
            name='Stock_availability',
        ),
    ]
