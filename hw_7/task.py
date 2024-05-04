"""
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в
конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование
должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.""

"""

import os
import re


def batch_rename_files(target_name, digits_count, src_ext, dest_ext,
                       name_range):
    """
    Функция для группового переименования файлов в каталоге.

    Args:
        target_name (str): Желаемое конечное имя файлов.
        digits_count (int): Количество цифр в порядковом номере.
        src_ext (str): Расширение исходных файлов для переименования.
        dest_ext (str): Расширение конечных файлов после переименования.
        name_range (tuple): Диапазон сохраняемого оригинального имени в виде 
        (start, end).
    """
    files = [f for f in os.listdir() if f.endswith(src_ext)]
    counter = 1
    for file in files:
        base_name, _ = os.path.splitext(file)
        orig_name = base_name[name_range[0] - 1:name_range[1]]
        new_name = f"{target_name}{orig_name}{str(counter).zfill(digits_count)}.{dest_ext}"
        os.rename(file, new_name)
        counter += 1


# Пример использования
if __name__ == '__main__':
    batch_rename_files("image_", 3, ".jpg", ".png", (3, 6))

