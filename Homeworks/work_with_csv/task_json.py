"""
Task 2, json.

Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є
валідними json. Pезультат для невалідного файлу виведіть
через логер на рівні еррор у файл json__<your_second_name>.log
"""

import json
import logging

logging.basicConfig(filename='json_Nazarenko.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def validate_json(filename):
    """валідуємо json."""
    try:
        with open(filename, 'r') as file:
            json.load(file)
        print(f'VALID: {filename}.')
    except json.JSONDecodeError as e:
        logging.error(f'Invalid JSON in file {filename}: {e}')
        print(f'ERROR: {filename}.')


json_files = ['localizations_en.json', 'localizations_ru.json',
              'login.json', 'swagger.json']
for json_file in json_files:
    validate_json(json_file)
