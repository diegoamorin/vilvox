# Generated by Django 2.0 on 2019-01-31 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('img', models.ImageField(upload_to='images/gamers/')),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('img', models.ImageField(upload_to='images/teams/')),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('img', models.ImageField(upload_to='images/videogames/')),
                ('category', models.CharField(max_length=50)),
                ('launch', models.DateField()),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='videogames',
            field=models.ManyToManyField(related_name='teams', to='wiki.VideoGame'),
        ),
        migrations.AddField(
            model_name='gamer',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='wiki.Team'),
        ),
        migrations.AddField(
            model_name='gamer',
            name='videogames',
            field=models.ManyToManyField(related_name='gamers', to='wiki.VideoGame'),
        ),
    ]
