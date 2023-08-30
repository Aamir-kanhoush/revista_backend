# Generated by Django 4.2.4 on 2023-08-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reaction',
            field=models.IntegerField(blank=True, choices=[(2, 'love'), (6, 'angry'), (4, 'wow'), (3, 'haha'), (1, 'like'), (5, 'sad')], null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('image', 'Image'), ('text', 'Text'), ('voice_record', 'Voice Record')], max_length=20),
        ),
    ]
