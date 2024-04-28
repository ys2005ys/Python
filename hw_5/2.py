""" 
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

# импортируем моудль для работы с путями
import os 


# В функции используем метод os.path.split(file_path) для разделения пути на
#  директорию и полное имя файла (с расширением).
#  Затем используем метод os.path.splitext(full_file_name) 
# для разделения полного имени файла на имя и расширение.
def get_path_info(file_path):
    directory, full_file_name = os.path.split(file_path)
    name, extension = os.path.splitext(full_file_name)
    return directory, name[1:], extension


# Пример использования
file_path = "/home/user/Documents/example.txt"
path, name, ext = get_path_info(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", ext)
