# Generated by Django 3.2.8 on 2021-10-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_user_user1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='subscription_time',
            field=models.CharField(max_length=100),
        ),
    ]
