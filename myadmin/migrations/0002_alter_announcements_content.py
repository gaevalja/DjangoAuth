# Generated by Django 4.0.6 on 2022-08-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
