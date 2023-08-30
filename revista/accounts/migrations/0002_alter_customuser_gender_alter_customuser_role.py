# Generated by Django 4.2.4 on 2023-08-10 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('moderator', 'Moderator'), ('regular-user', 'Regular User'), ('admin', 'Admin')], default='regular-user', max_length=25),
        ),
    ]
