# Generated by Django 4.1.3 on 2024-08-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborsbountyapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventTime',
            field=models.TimeField(),
        ),
    ]
