# Generated by Django 2.0 on 2019-02-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_name',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
    ]
