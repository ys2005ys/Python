"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с 
псевдо именами и произведением чисел.Напишите функцию, которая создаёт 
из созданного ранее файла новый с данными в формате JSON. 
Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки.
"""

import json


def to_json(file_name='res.txt'):
    with open(file_name, 'r', encoding='utf-8') as f, \
         open('res.json', 'w', encoding='utf-8') as f_jsom:
        all_data = []
        for line in f:
            all_data.append(line.capitalize())
        json.dump(all_data, f_jsom, indent=4)


if __name__ == '__main__':
    to_json()
