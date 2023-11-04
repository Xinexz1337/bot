import requests
from bs4 import BeautifulSoup
import time

url = 'https://cryptonews.net/ru/'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# caly site
post = soup.find("div", class_='row news-item start-xs').text
#print(post)


title = soup.find("div", class_='row news-item start-xs').text.strip()
url = soup.find("a", class_='image-wrap col-xs-12 col-sm-3', href=True)['href'].strip()
#title = title.replace(" ", "")  # Удалить пробелы из заголовка
#url = url.replace(" ", "")      # Удалить пробелы из URL
print(title + ' назад.' + "\nhttps://cryptonews.net" + url + '\nby. @daniil_adams')


