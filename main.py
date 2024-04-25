#rus - импорт всех ресурсов. telebot является частью библиотеки pyTelegramBotAPI, перед использованием установите эту библиотеку с помощью pip
#eng - importing all resources. Object "telebot" is part of library "pyTelegramBotAPI", install this library from pip before use

import os
import telebot
import qrcode
import config

#rus - Создание экземпляра класса telebot. Первым идет токен, полученный у BotFather, далее указана разметка ля текста с помощью HTML
#eng - Initializing instance of class telebot. In arguments first is token from BotFather, second - marking all text using HTML
bot = telebot.TeleBot(config.token, parse_mode = config.parse)

#rus - команда для запуска бота
#eng - Handler for command '/start', that turning bot on
@bot.message_handler(commands = ['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Привет, я - <strong>Бот - Генератор QR-кодов</strong>. \nНапиши мне любой текст, а дальше я все сделаю сам 💪 😉.')

#rus - команда помощи. Здесь указаны все необходимое + контакты разработчика (меня то есть)
#eng - Handler for command '/help', that gives some instructions + contacts of developer
@bot.message_handler(commands = ['help'])
def helper(message):
	bot.send_message(message.chat.id, '*Для начала работы напишите любой текст, и бот автоматически его превратит в QR-код.\n*Если случайно использовали недоступные символы - то не расстраивайтесь, бот автоматически их отклонит.\n*Хотите задать вопрос или оставить отзыв? Тогда пишите разработичку:\n@alexkaravdev')

#rus - получение текста и преобразование его в код. Дабы бот не путался при загрузке изображения, каждое изображение подписывается id того чата, в которой оно должно быть отправлено
#eng - Receiving and turning it into QR-Code. So that bot does not by mistake send user the wrong image, every image is getting name 'message.chat.id', that contains an id of a chat with user
@bot.message_handler(content_types = ['text'])
def create_code(message):
	bot.reply_to(message, 'Текст принят.\nНачинаю генерацию кода 🔨')
	data = message.text.encode('utf-8')
	filename = str(message.chat.id)
	img = qrcode.make(data)
	img.save(filename)
	photo = open(filename, 'rb')
	bot.send_message(message.chat.id, 'Готово! Твой код собран и готов к использованию🎉')
	bot.send_photo(message.chat.id, photo)
	photo.close()
	os.remove(filename)
	bot.send_message(message.chat.id, 'Спасибо за использование! Надеюсь вам понравилось😊 ')

#rus - запуск бота
#eng - Bot Launch
bot.polling(none_stop = True)