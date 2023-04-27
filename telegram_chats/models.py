from django.db import models
from telegram_chats.storage import OverwriteStorage


class KeyWord(models.Model):
    word_name = models.CharField(max_length=100)

    def __str__(self):
        return self.word_name


class AntiKeyWord(models.Model):
    word_name = models.CharField(max_length=100)

    def __str__(self):
        return self.word_name


class MinusWord(models.Model):
    minus_word_name = models.CharField(max_length=100)

    def __str__(self):
        return self.minus_word_name


class GroupChat(models.Model):
    input_chat_link = models.CharField(max_length=100)
    output_chat_link = models.CharField(max_length=100)
    keywords = models.ManyToManyField(KeyWord)
    anti_keywords = models.ManyToManyField(AntiKeyWord, blank=True, null=True)


class SessionCredentials(models.Model):
    api_id = models.CharField(max_length=100)
    api_hash = models.CharField(max_length=100)
    session_file = models.FileField(blank=True, null=True, storage=OverwriteStorage())
