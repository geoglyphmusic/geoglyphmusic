# Generated by Django 3.1.4 on 2021-01-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20201022_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]