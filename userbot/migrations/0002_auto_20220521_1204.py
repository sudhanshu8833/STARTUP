# Generated by Django 2.2.14 on 2022-05-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bnbusdt',
            name='time',
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='btcusdt',
            name='time',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ethusdt',
            name='time',
            field=models.FloatField(default=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solusdt',
            name='time',
            field=models.FloatField(default=434),
            preserve_default=False,
        ),
    ]
