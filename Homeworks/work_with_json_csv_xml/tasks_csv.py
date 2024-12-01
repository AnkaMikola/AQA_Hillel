"""
Task 1, csv.

Візміть два файли з теки ideas_for_test/work_with_json_csv_xml порівняйте на
наявність дублікатів і приберіть їх. Результат запишіть
у файл result_<your_second_name>.csv
"""

import csv

file1 = 'random.csv'
file2 = 'r-m-c.csv'
output_file = 'result_Nazarenko.csv'


def read_csv(file_path):
    """Read files."""
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv(file_path, data):
    """Write scv files."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def compare_and_write(file1, file2, output_file):
    """Compare and write function."""
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    combined_data = data1 + data2
    unique_data = [
        list(item) for item in {tuple(sublist)for sublist in combined_data}
    ]

    write_csv(output_file, unique_data)
    print(f"Unique data from files '{file1}' and '{file2}'"
          f" was wrote to a file '{output_file}'.")


compare_and_write(file1, file2, output_file)

"""write_csv(output_file, unique_data)
This should be orginized as separate function that accepts
two files - do comparison and writes output to file."""
