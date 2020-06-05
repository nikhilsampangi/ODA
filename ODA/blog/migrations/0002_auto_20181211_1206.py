# Generated by Django 2.1.2 on 2018-12-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textinblog',
            name='picture',
            field=models.ImageField(default='None.png', null=True, upload_to='MEDIA/blog/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='textinblog',
            name='the_sub',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
    ]