# Generated by Django 2.1.2 on 2018-12-11 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181211_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinblog',
            name='picture',
            field=models.ImageField(blank=True, default='None.png', upload_to='MEDIA/blog/%Y/%m/%d'),
        ),
    ]
