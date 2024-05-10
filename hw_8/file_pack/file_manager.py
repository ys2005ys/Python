"""
Прочитайте созданный в прошлом задании csv файл без использования 
csv.DictReader. Распечатайте его как pickle строку.
"""

import csv
import pickle
from pathlib import Path


def csv2pickles(file: Path) -> None:
    pickle_list = []
    with open(file, 'r', newline='', encoding='utf-8') as f:
        csv_file = csv.reader(f, dialect='excel-tab')
        for i, line in enumerate(csv_file):
            if i == 0:
                pickle_keys = line
            else:
                pickle_dict = {k: v for k, v in zip(pickle_keys, line)}
                pickle_list.append(pickle_dict)

    print(pickle.dumps(pickle_list))


if __name__ == '__main__':
    csv2pickles(Path('new_users.csv'))