# Generated by Django 4.1.3 on 2024-08-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborsbountyapi', '0002_alter_event_eventtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='uid',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
