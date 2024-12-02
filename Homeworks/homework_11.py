"""
Homework 11.1.

Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію
для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging

import pytest


def read_file(log_level, message):
    """
    Read file.

    :param log_level: logging level
    :param message: message text
    """
    expected_result = f'{log_level} - {message}'
    with open('homework11_login_system.log', 'r') as file:
        text_in_file = file.readlines()
        len_text_file = len(text_in_file)
        actual_result = text_in_file[len_text_file - 1]
        actual_result = ' - '.join(actual_result.split(' - ')[1:])
        assert actual_result[:-1] == expected_result


@pytest.mark.parametrize('username, status', [
    ('Alice', 'success'),
    ('Mykola', 'expired'),
    ('Taras', 'failed'),
])
def test_log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу:
    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити,
    логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f'Login event - Username: {username}, Status: {status}'

    # Створення та налаштування логера
    logging.basicConfig(
        filename='homework11_login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True,
    )
    logger = logging.getLogger('log_event')

    # Логування події
    if status == 'success':
        logger.info(log_message)
    elif status == 'expired':
        logger.warning(log_message)
    else:
        logger.error(log_message)

    log_name = None
    if status == 'success':
        log_name = 'INFO'
    elif status == 'expired':
        log_name = 'WARNING'
    elif status == 'failed':
        log_name = 'ERROR'

    read_file(log_level=log_name, message=log_message)
