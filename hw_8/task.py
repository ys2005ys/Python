"""
2. Напишите функцию, которая получает на вход директорию и рекурсивно обходи
её и все вложенные директории.
 Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов 
в ней с учётом всех вложенных файлов и директорий.
"""


import os
import json
import csv
import pickle


def get_directory_info(directory):
    result = []

    # Рекурсивная функция для обхода директорий и файлов
    def traverse_directory(directory):
        files = []
        directories = []

        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)

            if os.path.isfile(path):
                size = os.path.getsize(path)
                files.append({
                    'name': filename,
                    'type': 'file',
                    'size': size
                })
            elif os.path.isdir(path):
                info = traverse_directory(path)
                size = sum(entry['size'] for entry in info) if info else 0
                directories.append({
                    'name': filename,
                    'type': 'directory',
                    'size': size,
                    'content': info
                })

        result.extend(files)
        result.extend(directories)

        return files + directories

    traverse_directory(directory)

    # Сохранение результатов в файлы
    with open('result.json', 'w') as json_file:
        json.dump(result, json_file, indent=4)

    with open('result.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'type', 'size'])

        for entry in result:
            writer.writerow([entry['name'], entry['type'], entry['size']])

    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(result, pickle_file)

    return result


if __name__ == '__main__':
    get_directory_info("./hw_8")
