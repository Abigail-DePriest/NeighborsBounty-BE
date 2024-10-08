# Generated by Django 4.1.3 on 2024-09-12 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborsbountyapi', '0006_remove_inventory_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='neighborsbountyapi.inventory'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='pickupDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='pickupLocation',
            field=models.CharField(blank=True, default='Unknown', max_length=200),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
