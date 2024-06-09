from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests

def parse():
    url = 'https://www.pepper.ru/hot'
    headers = {   # отправляем запрос методом GET , чтобы избежать блокировки(у меня блокирует)
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")

    offers = soup.findAll('article', class_='thread')
    for offer in offers:
        title = offer.find('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title').get_text(strip=True)
        # находим и записываем название акции
        degrees = offer.find('span', class_='cept-vote-temp vote-temp vote-temp--hot').get_text(strip=True)
        # находим и записываем градусы
        link = offer.find('a', class_='cept-tt thread-link linkPlain thread-title--list js-thread-title')['href']
        # находим и записываем ссылку на акцию

        full_link = 'https://www.pepper.ru' + link

        # выводим данные в консоль
        print(f'Название акции: {title}')
        print(f'Градусы: {degrees}')
        print(f'Ссылка на акцию: {full_link}')
        print('-' * 40)

# вызываем функцию для выполнения парсинга
parse()

