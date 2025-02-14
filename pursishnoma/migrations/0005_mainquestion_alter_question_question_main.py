# Generated by Django 5.0.2 on 2024-03-16 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pursishnoma', '0004_question_question_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_main', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='question_main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pursishnoma.mainquestion'),
        ),
    ]
