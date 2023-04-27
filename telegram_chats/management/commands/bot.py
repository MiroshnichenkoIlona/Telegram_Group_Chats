from django.core.management.base import BaseCommand
from telethon import TelegramClient, events
from telegram_chats.models import KeyWord, MinusWord, GroupChat, SessionCredentials
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_groupping.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


session_credentials = SessionCredentials.objects.all().last()
api_id = session_credentials.api_id
api_hash = session_credentials.api_hash
session_file = 'new_session'

client = TelegramClient(session_file, api_id, api_hash)

client.start()


def keywords_handler(text):
    keywords = list(KeyWord.objects.all())
    for keyword in keywords:
        if keyword.word_name.lower() in text.lower():
            return keyword
    return False


def group_anti_keywords_handler(anti_keywords, text):
    print('1')
    for keyword in anti_keywords:
        print('2')
        if keyword.word_name.lower() in text.lower():
            return True
    return False


def anti_keywords_handler(text):
    anti_keywords = list(MinusWord.objects.all())
    for anti_keyword in anti_keywords:
        if anti_keyword.minus_word_name.lower() in text.lower():
            return True
    return False


def correspondence_check_by_keyword(filter_link, keyword):
    chat_filter = list(GroupChat.objects.filter(input_chat_link=filter_link, keywords__in=[keyword]))
    if len(chat_filter) == 0:
        return False
    return chat_filter[0]


async def send_into_output_chat(output_link, final_message_for_chat):
    output_chat = await client.get_entity(output_link)
    await client.send_message(output_chat, final_message_for_chat)


@client.on(events.NewMessage())
async def handle_new_message(event):
    text = event.message.text

    if anti_keywords_handler(text):
        return

    sender = await event.get_sender()
    chat = await event.get_chat()
    keyword = keywords_handler(text)

    if keyword is False:
        return

    filter_link = "t.me/" + event.chat.username
    message_link = f'https://t.me/{chat.username}/{event.id}'
    final_message_for_chat = '@' + sender.username + '\n' + text + '\n' + message_link + '\n' + filter_link + '\n' + 'keyword: ' + keyword.word_name
    group_chat = correspondence_check_by_keyword(filter_link, keyword)

    if group_chat is False:
        return
    print('sa')
    if group_anti_keywords_handler(group_chat.anti_keywords.all(), text):
        print('sad')
        return

    await send_into_output_chat(group_chat.output_chat_link, final_message_for_chat)


class Command(BaseCommand):
    help = 'ТГ бот для анализа'

    def handle(self, *args, **options):
        client.run_until_disconnected()
