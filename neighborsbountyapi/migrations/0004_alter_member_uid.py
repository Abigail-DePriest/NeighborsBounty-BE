# Generated by Django 4.1.3 on 2024-08-27 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborsbountyapi', '0003_alter_member_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='uid',
            field=models.CharField(max_length=50),
        ),
    ]
