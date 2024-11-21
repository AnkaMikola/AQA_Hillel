"""
Task 3, xml.

Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію
пошуку по group/number і повернення значення timingExbytes/incoming.
Pезультат виведіть у консоль через логер на рівні інфо
"""

import logging

from lxml import etree

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def find_incoming_by_group_number(xml_file, group_number):
    """шукаємо incoming."""
    try:
        tree = etree.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('.//group'):
            number = group.find('number').text
            if number == str(group_number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        logging.info(f'Group {group_number}: '
                                     f'Incoming value = {incoming.text}')
                        return incoming.text
                logging.info(f'Group {group_number}: '
                             f'"timingExbytes/incoming" not found.')
                return None
        logging.info(f'Group {group_number} not found in the XML.')
        return None
    except Exception as e:
        logging.error(f'Error parsing XML file: {e}')
        return None


find_incoming_by_group_number('groups.xml', 4)
