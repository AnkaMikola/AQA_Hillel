"""
19.2 POST/GET/DELETE.

У venv Python встановiть Flask за допомогою команди pip install flask

Створiть у окремiй директорiї файл app.py та скопiюйте у нього
код файлу app.py який приведено нижче в початкових даних.

Запустiть http сервер за допомогою команди python app.py

Сервер стартує за базовою адресою http://127.0.0.1:8080

Враховуючи документацiю яку наведено нижче вам потрiбно написати
код, який використовуючи модуль request
1) зробить через POST upload якогось зображення на сервер,
2) за допомогою GET отримає посилання на цей файл и потiм
3) за допомогою DELETE зробить видалення файлу з сервера.

Документацiя для  app.py

Cерверна частина надає можливість завантажувати,
отримувати та видаляти зображення.
-------------------------------------------------------------------------------------
Завантаження зображення
Метод: POST
Шлях: /upload
Опис: Завантажує зображення на сервер.

Параметри запиту:
image: файл зображення (тип MIME: image/*)
Відповідь:
Код стану 201 (Created) у разі успішного завантаження.
Повертає URL завантаженого зображення у форматі JSON:

{
    "image_url": "<http://127.0.0.1:8080/uploads/example.jpg>"
}
-------------------------------------------------------------------------------------
Отримання URL завантаженого зображення
Метод: GET
Шлях: /image/<filename>
Опис: Повертає URL або саме зображення в залежності від
заголовка Content-Type. **<filename>** повинен бути вказаним
враховуючи правила кодування ULR

Відповідь:
- Код стану 200 (OK)
- Повертає URL завантаженого зображення у форматі JSON,
якщо Content-Type рівний text:

{
    "image_url": "<http://127.0.0.1:8080/uploads/example.jpg>"
}

- Повертає саме зображення, якщо Content-Type рівний image.
-------------------------------------------------------------------------------------
Видалення зображення
Метод: DELETE
Шлях: /delete/<filename>
Опис: Видаляє завантажене зображення з серверу. **<filename>** повинен
бути вказаним враховуючи правила кодування ULR

Відповідь:
Код стану 200 (OK) у разі успішного видалення.
Повертає повідомлення про успішне видалення у форматі JSON:
{
    "image_url": "http://127.0.0.1:8080/uploads/example.jpg"
}
"""

import requests

URL = 'http://127.0.0.1:8080'
image_path = 'uploads/image.jpg'


def upload_image(image_path):
    """Upload image to server."""
    with open(image_path, 'rb') as img:
        files = {'image': img}
        response = requests.post(f'{URL}/upload', files=files, timeout=5)

    if response.status_code == 201:
        image_url = response.json().get('image_url')
        print(f'Зображення успішно завантажено: {image_url}')
        return image_url
    else:
        print(f'Помилка завантаження зображення: {response.status_code}')
        print(response.text)
        return None


def get_image_url(filename):
    """Get URL."""
    response = requests.get(f'{URL}/image/{filename}',
                            headers={'Content-Type': 'text'},
                            timeout=5)

    if response.status_code == 200:
        image_url = response.json().get('image_url')
        print(f'URL зображення: {image_url}')
        return image_url
    else:
        print(f'Помилка отримання URL: {response.status_code}')
        print(response.text)
        return None


def delete_image(filename):
    """Delete image."""
    response = requests.delete(f'{URL}/delete/{filename}', timeout=5)

    if response.status_code == 200:
        print(f'Зображення успішно видалено: '
              f"{response.json().get('image_url')}")
    else:
        print(f'Помилка видалення зображення: {response.status_code}')
        print(response.text)


# Основна програма
if __name__ == '__main__':
    # Крок 1: Завантаження зображення
    uploaded_image_url = upload_image(image_path)

    if uploaded_image_url:
        # Витягування імені файлу з URL
        filename = uploaded_image_url.split('/')[-1]

        # Крок 2: Отримання URL завантаженого зображення
        get_image_url(filename)

        # Крок 3: Видалення зображення
        delete_image(filename)
