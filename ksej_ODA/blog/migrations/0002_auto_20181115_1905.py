# Generated by Django 2.1.2 on 2018-11-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinblog',
            name='the_sub',
            field=models.TextField(default='None', null=True),
        ),
    ]
