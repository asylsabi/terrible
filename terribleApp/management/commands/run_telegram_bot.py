from django.core.management.base import BaseCommand
import telebot
from terribleApp.models import Books
bot = telebot.TeleBot("6735627422:AAEyHeZREkevHVH7Df9ceK7Kv-xG2Vh4BH4")
all_commands = ['/start', '/help', '/books']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")


@bot.message_handler(commands=['books'])
def books(message):
    all_books = Books.objects.all()
    for book in all_books:
        message_text = f"{book.name}: {book.price} тг"
        bot.send_message(message.chat.id, message_text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")


@bot.message_handler(commands=['help'])
def help_command(message):
    command_list = "\n".join(all_commands)
    help_message = f"Вот все команды:\n{command_list}"
    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['add'])
def add(message):
    bot.send_message(message.from_user.id, "Введи название")
    bot.register_next_step_handler(message, title_handler)


def title_handler(message):
    global title
    title = message.text

    bot.send_message(message.chat.id, "Напиши цену")
    bot.register_next_step_handler(message, price_handler)


def price_handler(message):
    global price
    price = message.text
    bot.send_message(message.chat.id, f"Новая книга успешно добавлена")
    new_game = Books.objects.create(name=title, price=price)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



