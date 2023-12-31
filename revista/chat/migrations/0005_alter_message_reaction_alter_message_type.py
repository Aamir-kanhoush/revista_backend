# Generated by Django 4.2.4 on 2023-08-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_reaction_alter_message_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reaction',
            field=models.IntegerField(blank=True, choices=[(1, 'like'), (2, 'love'), (3, 'haha'), (4, 'wow'), (5, 'sad'), (6, 'angry')], null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('voice_record', 'Voice Record')], max_length=20),
        ),
    ]
