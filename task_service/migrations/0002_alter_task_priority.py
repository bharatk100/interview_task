# Generated by Django 4.2.11 on 2024-04-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=191, null=True),
        ),
    ]
