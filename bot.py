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
    bot.send_message(message.chat.id, 'Ответы на некоторые вопросы могут отличатся пособом ответа для разнообразия. Если этот способ будет не практичен, либо не удобен, можно связатся со мной тут: https://t.me/Igorpq')
    bot.send_message(message.chat.id, 'Первый проходной вопрос: В чём разница между списком и кортежем?', reply_markup = keyboard)

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    true_answer = 0
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'Все команды для управления ботом:\n/questions - Показать список всех вопросов\n/add_question - Предложить добавить вопрос\n/exit - Показать отвеченные вопросы')
    if message.text == '/questions':
        bot.send_message(message.from_user.id, 'Все вопросы:\n/1 Что такое язык программирования?\n/2 есть ли в python функция main()?\n/3 Что такое декораторы в Python?\n/4 Как используется оператор // в Python?\n/5 Как используется %s?\n/6 Обязательно ли функция Python должна возвращать значение?\n/7 В чем разница между модулем и пакетом в Python?\n/8 что означает «self» в Python?\n/9 Каковы ключевые особенности Python?\n/10 Как изменить тип данных списка?')
    if message.text == '/1':
        bot.send_message(message.chat.id, 'Что такое язык программирования?\n/one Язык программирования  формальный язык, предназначенный для записи компьютерных программ.\n/two Это язык разметки')
    if message.text == '/one':
        bot.send_message(message.chat.id, 'Верно! Починете мне принтер? Вы же программист. Может тогда взломаете мне чужой вк? ')
        true_answer += 1
    elif message.text == '/two':
        bot.send_message(message.chat.id, 'Нет, не верно')
    if message.text == '/2':
        bot.send_message(message.chat.id, 'есть ли в python функция main()? /yes - Да /no - Нет')
    if message.text == '/yes':
        bot.send_message(message.chat.id, 'Да, верно! И да, если вы дошли до этого вопроса, то у вас есть выбор: ломать логику бота(думаю это не то, что сейчас стоит внимания) либо следовать логике написания бота и после всех вопросов крушить, ломать всё и похвастатся об этом мне и я это исправлю(бесплатные тестеры)')
        true_answer += 1
    elif message.text == '/no':
        bot.send_message(message.chat.id, 'Ну... Думаю удача вам пригодится)')
    if message.text == '/3':
        bot.send_message(message.chat.id, 'Что такое декораторы в Python? \n/y Это сложная формула, которая подходит для всех задач\n/n Декоратор - паттерн проектирования, при использовании которого класс или функция изменяет или дополняет функциональность другого класса или функции без использования наследования или прямого изменения исходного кода.')
    if message.text == '/y':
        bot.send_message(message.chat.id, 'нет, не угадали(')
    elif message.text == '/n':
        bot.send_message(message.chat.id, 'хахаха, верно!')
        true_answer += 1
    if message.text == '/4':
        bot.send_message(message.chat.id,'Как используется оператор // в Python? /q используется он для деления без остатка /p Данный оператор делит на дробные числа')
    if message.text == '/q':
        bot.send_message(message.chat.id,'И снова правильно.')
        true_answer += 1
    elif message.text == '/p':
        bot.send_message(message.chat.id,'не-а...')
    if message.text == '/5':
        bot.send_message(message.chat.id, 'Верно ли утверждение о том как используется %s? %s, он специально используется для объединения двух или более строк в Python. %s позволяет нам форматировать или помещать строку или числовое значение в заданную строку /true - правда /false - не правда')
    if message.text == '/true':
        bot.send_message(message.chat.id, 'Верно!')
        true_answer += 1
    elif message.text == '/false':
        bot.send_message(message.chat.id, 'Не верно.')
    if message.text == '/6':
        bot.send_message(message.chat.id, 'Обязательно ли функция Python должна возвращать значение? /ye /nn')
    if message.text == '/nn':
        bot.send_message(message.chat.id, 'нет, не верно...')
    elif message.text == '/ye':
        bot.send_message(message.chat.id, 'Верно! возвращаемые значения обязательны с точки зрения внутреннего устройства Python. Если вы даже попытаетесь написать функцию, которая не возвращает значения – не сможете. Если функция даже не станет возвращать значения, то интерпретатор Python «принудит» ее возвращать None.')
        true_answer += 1
    if message.text == '/7':
        bot.send_message(message.chat.id, 'В чем разница между модулем и пакетом в Python? /da пакет это набор модулей Python: в то время как модуль представляет собой один файл Python, пакет представляет собой каталог модулей Python, содержащий дополнительный __init__.py файл, чтобы отличить пакет от каталога, который просто содержит кучу скриптов Python. /daa Разницы нету')
    if message.text == 'da':
        bot.send_message(message.chat.id, 'Верно')
        true_answer += 1
    elif message.text == 'daa':
        bot.send_message(message.chat.id, 'Не верно')
    if message.text == '/8':
        bot.send_message(message.chat.id, 'что означает «self» в Python? /its Аргумент self в Python ссылается на сам объект. Self - это имя, предпочитаемое соглашением Pythons для обозначения первого параметра методов экземпляра в Python /or_its Self - это импортируемая библеотека python.')
    if message.text == '/its':
        bot.send_message(message.chat.id, 'Верно')
        true_answer += 1
    elif message.text == 'or_its':
        bot.send_message(message.chat.id, 'Не верно')
    if message.text == '/9':
        bot.send_message(message.chat.id, 'Каковы ключевые особенности Python? /yes_1 изкий порог входа, быстро работает, самое то для серьёзных проектов и для новичков /yes_2 Его особенность в том, что на python лучше писать короткие но функциональные программы')
    if message.text == '/yes_1':
        bot.send_message(message.chat.id, 'Верно')
        true_answer += 1
    elif message.text == '/yes_2':
        bot.send_message(message.chat.id, 'Не верно')
    if message.text == '/10':
        bot.send_message(message.chat.id, 'Как изменить тип данных списка? /tru_1 Можно поменять тип данных с помощью int(), str(), float() и.т.д /tru_2 Изменить тип данных в python нельзя.')
    if message.text == '/tru_1':
        bot.send_message(message.chat.id, 'Верно')
        true_answer += 1
    elif message.text == '/tru_2':
        bot.send_message(message.chat.id, 'Не верно')
    if message.text == '/exit':
        bot.send_message(message.chat.id, true_answer)
@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.data == 'button 1':
        bot.send_message(call.message.chat.id, 'Ответ не верный...')
    if call.data == 'button 2':
        bot.send_message(call.message.chat.id, 'Вы ответили верно!')
    if call.data == 'button 3':
        bot.send_message(call.message.chat.id,line)
bot.polling(non_stop=True, interval= 0)
