"""
Task 1, csv
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на
наявність дублікатів і приберіть їх. Результат запишіть
у файл result_<your_second_name>.csv
"""

import csv

# Шляхи до файлів
file1 = "random.csv"
file2 = "r-m-c.csv"
output_file = "result_Nazarenko.csv"

# Функція для зчитування даних з файлу
def read_csv(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        return list(reader)

# Функція для запису даних у файл
def write_csv(file_path, data):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


data1 = read_csv(file1)
data2 = read_csv(file2)

combined_data = data1 + data2

unique_data = list(map(list, set(map(tuple, combined_data))))

write_csv(output_file, unique_data)
