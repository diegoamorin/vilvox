# Generated by Django 2.0 on 2019-03-18 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190224_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fullname',
        ),
    ]
