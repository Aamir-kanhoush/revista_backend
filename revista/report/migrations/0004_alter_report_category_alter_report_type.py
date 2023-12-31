# Generated by Django 4.2.4 on 2023-08-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_alter_report_category_alter_report_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('harassment', 'Harassment'), ('spam', 'Spam'), ('inappropriate-content', 'Inappropriate content')], max_length=25),
        ),
        migrations.AlterField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('user', 'User'), ('post', 'Post'), ('chat', 'Chat')], max_length=25),
        ),
    ]
