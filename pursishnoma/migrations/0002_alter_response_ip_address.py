# Generated by Django 5.0.2 on 2024-03-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pursishnoma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='ip_address',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
