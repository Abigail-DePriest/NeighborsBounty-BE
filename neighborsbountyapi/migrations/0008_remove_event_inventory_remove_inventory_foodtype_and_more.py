# Generated by Django 4.1.3 on 2024-09-12 21:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neighborsbountyapi', '0007_event_inventory_alter_inventory_pickupdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='foodType',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='pickupDate',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='quantity',
        ),
        migrations.AddField(
            model_name='inventory',
            name='items',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='inventory',
            name='weekEndDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inventory',
            name='weekStartDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
