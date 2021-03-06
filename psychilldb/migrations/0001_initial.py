# Generated by Django 3.1.2 on 2020-10-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=120)),
                ('album', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('tempo', models.IntegerField()),
                ('key', models.CharField(max_length=20)),
                ('energy', models.IntegerField()),
            ],
        ),
    ]
