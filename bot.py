import random as r
import telebot
from telebot import types
print('Бот работает')

bot = telebot.TeleBot('5103694247:AAHzEGG6MxAQiM58-MLIH58Et5DZ08jd44U')
with open('questions.txt', 'r') as file:
    line = file.readline()
@bot.message_handler(commands = ['start'])

def start_messages(message):
    
    button3 = types.InlineKeyboardButton(text = 'можете выбрать случайный вопрос', callback_data = 'button 3')
    bot.send_message(message.from_user.id, 'Узнать как пользоватся ботом:\n/help')
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = 'Нет разницы', callback_data = 'button 1')
    button2 = types.InlineKeyboardButton(text = 'Список подвергается изменению, кортеж нет', callback_data = 'button 2')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)

    bot.send_message(message.chat.id, 'В чём разница между списком и кортежем?', reply_markup = keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Все команды для управления ботом:\n/questions - Показать список всех вопросов\n/add_question - Предложить добавить вопрос\n/exit - Показать отвеченные вопросы')


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'button 1':
        bot.send_message(call.message.chat.id, 'Ответ не верный...')
    if call.data == 'button 2':
        bot.send_message(call.message.chat.id, 'Вы ответили верно!')
    if call.data == 'button 3':
        bot.send_message(call.message.chat.id, line)
        print(r.choice(line))#это для проверки
bot.polling(non_stop=True, interval= 0)


