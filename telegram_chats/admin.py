from django.contrib import admin
from .models import KeyWord, AntiKeyWord, MinusWord, GroupChat, SessionCredentials


@admin.register(KeyWord)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('word_name',)
    search_fields = ('word_name',)


@admin.register(AntiKeyWord)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('word_name',)
    search_fields = ('word_name',)


@admin.register(MinusWord)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('minus_word_name',)
    search_fields = ('minus_word_name',)


@admin.register(GroupChat)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('input_chat_link', 'output_chat_link',)
    search_fields = ('input_chat_link', 'output_chat_link',)


@admin.register(SessionCredentials)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('api_id', 'api_hash',)
    search_fields = ('api_id', 'api_hash',)
