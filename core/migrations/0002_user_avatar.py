# Generated by Django 4.2.11 on 2024-04-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
