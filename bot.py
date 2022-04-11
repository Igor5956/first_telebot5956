import random as r
import telebot
from telebot import types
print('Бот работает')

bot = telebot.TeleBot('5103694247:AAHzEGG6MxAQiM58-MLIH58Et5DZ08jd44U')
with open('questions.txt', 'r') as file:
    lines = [i.strip() for i in file.readlines()]
    questions = '\n'.join(lines)
    print(questions)
d = {0: 'да', 1: 'да', 2:'да', 4:'нет', 5:'да', 6:'да', 7:'да', 8:'да', 9:'нет', 10:'да'}
num_question = 0

@bot.message_handler(commands = ['start'])
def start_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton('Да',callback_data='yes')
    button_no = types.InlineKeyboardButton('Нет', callback_data='no')
    keyboard.add(button_yes)
    keyboard.add(button_no)
    keyboard.row_width = 2
    num_question = r.randint(0, 9)
    bot.send_message(message.chat.id, lines[num_question], reply_markup=keyboard)

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Все команды для управления ботом:\n/questions - Показать список всех вопросов\n/add_question - Предложить добавить вопрос\n/exit - Показать отвеченные вопросы')
    if message.text == '/questions':
        questions = '\n'.join(lines)
        bot.send_message(message.from_user.id, questions)


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'yes':
        if d[num_question] == 'да':
            bot.send_message(call.message.chat.id, 'Все верно, молодец')
        else:
            bot.send_message(call.message.chat.id, 'Неверно...')
    if call.data == 'no':
        if d[num_question] == 'нет':
            bot.send_message(call.message.chat.id, 'Все верно, молодец')
    else:
        bot.send_message(call.message.chat.id, 'Неверно...')
bot.polling(non_stop=True, interval= 0)
