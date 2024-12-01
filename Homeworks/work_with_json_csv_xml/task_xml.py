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
                        return (f'Group {group_number}:'
                                f'Incoming value = {incoming.text}')
                    return (f'Group {group_number}:'
                            f'"timingExbytes/incoming" not found.')
                return f'Group {group_number} not found in the XML.'
    except Exception as e:
        return f'Error parsing XML file: {e}'


group_number = 4
result = find_incoming_by_group_number('groups.xml', group_number)

logging.info(result)
print(result)

"""
Please, ignor these lint warnings:

S410 Using etree to parse untrusted XML data is known to be vulnerable
to XML attacks. Replace etree with the equivalent defusedxml package.

S320 Using lxml.etree.parse to parse untrusted XML data is known to be
vulnerable to XML attacks. Replace lxml.etree.parse with its
defusedxml equivalent function.
"""
