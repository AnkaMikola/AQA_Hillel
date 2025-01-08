"""
19.1. Mars Rover “Curiosity” photos.

Є вiдкритий API NASA який дозволяє за певними параметрами
отримати данi у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi.

Серед цих даних є посилання на фото, якi потрiбно розпарсити i
за допомогою додаткових запитiв скачати i
зберегти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg.

Завдання потрiбно зробити використовуючи модуль requests
"""

import requests


def download_file(url, filename):
    """
    Завантажує і зберігає файл.

    :param url: Посилання на файл
    :param filename: Ім'я файлу для збереження
    """
    response = requests.get(url, stream=True, timeout=5)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f'Файл {filename} успішно завантажено.')
    else:
        print(f'Не вдалося завантажити файл {filename}. '
              f'Статус-код: {response.status_code}')


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
response = requests.get(url, params=params, timeout=5)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if photos:
        for i, photo in enumerate(photos, start=1):
            img_src = photo.get('img_src')
            if img_src:
                filename = f'mars_photo{i}.jpg'
                download_file(img_src, filename)
    else:
        print('Фото не знайдено для вказаного запиту.')
else:
    print(f'Помилка. Статус-код: {response.status_code}')
