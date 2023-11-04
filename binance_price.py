from binance.client import Client
import time
import schedule

from telebot import types
markup = types.InlineKeyboardMarkup()

api_key = 'uO6ByVkhmxoWHHuAXUgmiEFuNakkYFkiGB4yMKcKlVu4XUKo6iMUDDx3oIV0XXb5'
api_secret = '49MwArXtb9Br4oaE32QihamQPTxYtrfbvcA7icMs8Eezk5oWrWbSRzXKpq8vi6Zz'


#нужен для dir\main.py
spam = False


# Создаем клиент Binance
client = Client(api_key, api_secret)

# Получаем текущую цену Bitcoin (BTC)
#def get_current_price():
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
print(f"\n\nТекущая цена ETH ({ticker_symbol1}): {current_price1} USDT\n")
print(f"\n\nТекущая цена OP ({op_usdt}): {current_price3} USDT\n")
OP = f"\nТекущая цена OP ({op_usdt}): {current_price3} USDT"
BTCUSDT = f"Текущая цена Bitcoin ({ticker_symbol}): {current_price} USDT"
ETHUSDT = f"\n\nТекущая цена ETH ({ticker_symbol1}): {current_price1} USDT"



