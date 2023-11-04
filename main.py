import telebot
import types
from telebot import types
import requests
from bs4 import BeautifulSoup
import time
import schedule
import binance_price
from parser import url, title


bot = telebot.TeleBot('6509823360:AAH-CkpjqKIixLEXj1vGCvTevxKHyZKYrWE')
id_chanel = '@studianews'


#команда хелп
@bot.message_handler(commands=['help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    help = types.KeyboardButton('/start')
    markup.add(help)
    mess = '🛎️Если тебе нужна моя помощь, пиши сюда --> @daniil_adams'
    bot.send_message(message.chat.id, mess, reply_markup=markup)

#команда старт
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mess = '👋Привет друг, этот бот создан что бы смотреть самые свежие новости в этом @studianews тгк. ' \
           'Напиши "/chek" что бы посмотреть новости о Crypto.' \
           '\n\nЕсли тебя интересует крипта в срочном образе, тогда советую выбрать функцию "/send_crypto"' \
           'Эта функция будет тебе скидывать каждые 5 секунд обновлённую цену крипты' \
           '\n\n Если Вас интересует разовый подход, а не спам, тогда пропишите команду "/crypto"' \
           'Оно Вам покажет текущую цену крипты.' \
           '\n\n❗Если что то не понятно, пиши "/help"'
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    chek = types.KeyboardButton('/chek')
    markup.add(crypto_send, crypro_spam, chek, help)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


#отправка текущей цены крипты каждые 5 сек
@bot.message_handler(commands=['send_crypto'])
def crypto_spam(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        stop = types.KeyboardButton('/stop')
        markup.add(stop)
        mess = '❗Что бы остановить спам, напиши команду "/stop"'
        bot.send_message(message.chat.id, mess, reply_markup=markup)
        binance_price.spam = True
        while binance_price.spam:
                price_crypto()
                time.sleep(5)

#система команды стоп
@bot.message_handler(commands=['stop'])
def stop(message):
    if binance_price.spam == False:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        chek = types.KeyboardButton('/chek')
        help = types.KeyboardButton('/help')
        crypro_spam = types.KeyboardButton('/send_crypto')
        crypto_send = types.KeyboardButton('/crypto')
        markup.add(crypto_send, crypro_spam, chek, help)
        bot.send_message(message.chat.id, '‼️ Не понял команды, выбери команду которую хочешь использовать', reply_markup=markup)

    while binance_price.spam == True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        chek = types.KeyboardButton('/chek')
        help = types.KeyboardButton('/help')
        crypro_spam = types.KeyboardButton('/send_crypto')
        crypto_send = types.KeyboardButton('/crypto')
        markup.add(crypto_send, crypro_spam, chek, help)
        mess = ("✔Остановился :)" + "\nМогу ли я тебе ещё чем-то помочь, если да, то" +
                                        " выбери любую тебе подходящую функцию. "
                                        "\nЛибо выбери '/help' для помощи")
        bot.send_message(message.chat.id, mess, reply_markup=markup)
        binance_price.spam = False



#cammands chek
@bot.message_handler(commands=['chek'])
def chek(message):
    bot.send_message(message.from_user.id, f"📄 Вся информация с новостями тут --> {id_chanel} 📄")
    bot.send_message(id_chanel, (title + f' назад.' + f"\nhttps://cryptonews.net" + url + f'\n\n🤖by. @daniil_adams'))
    price_crypto()
    time.sleep(1)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help)
    mess = ("⚠️Выбери другую функцию для продолжения использования бота.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)

#command сrypto
@bot.message_handler(commands=['crypto'])
def crypto(message):
    bot.send_message(message.from_user.id, "📄 Вся информация с новостями тут --> @studianews 📄")
    price_crypto()
    time.sleep(1)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, chek, help)
    mess = ("⚠️Выбери другую функцию для продолжения использования бота.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)



#шутка
@bot.message_handler(commands=['admin_on'])
def admin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    markup.add(start)
    mess = ("🐓 Наебали Вас <3 🐓")
    bot.send_message(message.chat.id, mess, reply_markup=markup)


#обработка на отправку гиф
@bot.message_handler(content_types=['animation'])
def handle_gif(message):
    bot.send_message(message.chat.id, "🖼️ Извините, но я не воспронимаю GIF 🖼️")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    chek = types.KeyboardButton('/chek')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)


#обработка на отправку кружочков
@bot.message_handler(content_types=['video_note'])
def handle_video_note(message):
    bot.send_message(message.chat.id, "🎥 Извините, но я не воспронимаю Video 🎥")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)

#обработка на отправку фото
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "📷 Извините, но я не воспронимаю Photo 📷")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)

#обработка на отправку видео
@bot.message_handler(content_types=['video'])
def handle_video(message):
    bot.send_message(message.chat.id, "🎥 Извините, но я не воспронимаю Video 🎥")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)


#обработка на отправку музыки
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    bot.send_message(message.chat.id, "🎧 Послушаю позже, а пока я занят, ммне надо работать :) 🎧")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)


#обработка на отправку голосовых сообщений
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.send_message(message.chat.id, "🎤 Извините, но я не воспронимаю Voice🎤")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)

#обработка на отправку document
@bot.message_handler(content_types=['document'])
def handle_document(message):
    bot.send_message(message.chat.id, "📄 Извините, но я не воспронимаю Documents 📄")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    start = types.KeyboardButton('/start')
    chek = types.KeyboardButton('/chek')
    help = types.KeyboardButton('/help')
    crypro_spam = types.KeyboardButton('/send_crypto')
    crypto_send = types.KeyboardButton('/crypto')
    markup.add(crypto_send, crypro_spam, start, help, chek)
    mess = ("⚠️Выбери другую функцию.")
    bot.send_message(message.chat.id, mess, reply_markup=markup)



#директория всех сообщений и исправление команд.
@bot.message_handler(content_types=['text'])
def commands(message):
#Пишет в Канал "новости" то саме что пишу в бот
#bot.send_message(id_chanel, message.text)


    # argument
        if (message.text == "артур" ):
            with open('gif.mp4', 'rb') as video:
                bot.send_message(message.from_user.id, f"Jaka kurwa Alicija ?")
                bot.send_video(message.from_user.id, video)

        elif (message.text == 'Артур'):
            with open('gif.mp4', 'rb') as video:
                bot.send_message(message.from_user.id, f"Jaka kurwa Alicija ?")
                bot.send_video(message.from_user.id, video)


        elif (message.text == 'макс'):
            with open('рита.jpg', 'rb') as photo:
                bot.send_message(message.from_user.id, f"Как оцениаешь от 1 до 10?")
                bot.send_photo(message.from_user.id, photo)

        elif (message.text == 'Макс'):
            with open('рита.jpg', 'rb') as photo:
                bot.send_message(message.from_user.id, f"Как оцениаешь от 1 до 10?")
                bot.send_photo(message.from_user.id, photo)

        elif (message.text == 'максим'):
            with open('рита.jpg', 'rb') as photo:
                bot.send_message(message.from_user.id, f"Как оцениаешь от 1 до 10?")
                bot.send_photo(message.from_user.id, photo)

        elif (message.text == 'Максим'):
            with open('рита.jpg', 'rb') as photo:
                bot.send_message(message.from_user.id, f"Как оцениаешь от 1 до 10?")
                bot.send_photo(message.from_user.id, photo)


        elif (message.text == 'даня'):
                bot.send_message(message.from_user.id, f"Admin gamemode on")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                admin = types.KeyboardButton('/admin_on')
                markup.add(admin)
                mess = ("⚠️")
                bot.send_message(message.chat.id, mess, reply_markup=markup)

        elif (message.text == 'Даня'):
                bot.send_message(message.from_user.id, f"Admin gamemode on")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                admin = types.KeyboardButton('/admin_on')
                markup.add(admin)
                mess = ("⚠️")
                bot.send_message(message.chat.id, mess, reply_markup=markup)

        else:
            bot.send_message(message.from_user.id, "‼️ Я тебя не понимаю! Напиши команду '/chek', "
                                                 "что бы увидеть новые новости о Crypto.."
                                                 "\nЛибо комманду '/help' если нужна помощь ‼")




def parser(back_post_id, message):
    url = 'https://cryptonews.net/ru/'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # caly site
    post = soup.find("div", class_='row news-item start-xs', id=True).text
    # print(post)

    title = soup.find("div", class_='row news-item start-xs').text.strip()
    url = soup.find("a", class_='image-wrap col-xs-12 col-sm-3', href=True)['href'].strip()
    #print(title, "\nhttps://cryptonews.net" + url)



from binance.client import Client
def price_crypto():

    api_key = binance_price.api_key
    api_secret = binance_price.api_secret

    # Создаем клиент Binance
    client = Client(api_key, api_secret)

    # Получаем текущую цену Bitcoin (BTC)
    ticker_symbol = "BTCUSDT"  # Замените на символ торговой пары, которая вас интересует
    ticker_info = client.get_symbol_ticker(symbol=ticker_symbol)
    current_price = float(ticker_info["price"])

    ticker_symbol1 = "ETHUSDT"  # Замените на символ торговой пары, которая вас интересует
    ticker_info = client.get_symbol_ticker(symbol=ticker_symbol1)
    current_price1 = float(ticker_info["price"])

    op_usdt = "OPUSDT"
    ticker_info = client.get_symbol_ticker(symbol=op_usdt)
    current_price3 = float(ticker_info["price"])

    # Выводим текущую цену Bitcoin
    print(f"Текущая цена Bitcoin ({ticker_symbol}): {current_price} USDT")
    print(f"\n\nТекущая цена ETH ({ticker_symbol1}): {current_price1} USDT")
    BTCUSDT = f"Текущая цена Bitcoin ({ticker_symbol}): {current_price} USDT"
    ETHUSDT = f"\nТекущая цена ETH ({ticker_symbol1}): {current_price1} USDT"
    OP = f"\nТекущая цена OP ({op_usdt}): {current_price3} USDT"
    bot.send_message(id_chanel, f'{BTCUSDT} \n {ETHUSDT} \n {OP}')


bot.polling()
