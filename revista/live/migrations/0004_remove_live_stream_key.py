# Generated by Django 4.2.4 on 2023-08-17 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='live',
            name='stream_key',
        ),
    ]