# Generated by Django 4.2 on 2023-04-25 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_chats', '0003_sessioncredentials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupchat',
            name='minus_keywords',
        ),
        migrations.AddField(
            model_name='sessioncredentials',
            name='session_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
