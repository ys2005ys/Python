"""
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""


from pathlib import Path


def rename_group(new_name = "New", num = 2, extension="txt", extension_new="doc", old_name=[1, 5]):
    no_rename_extension = ["md", "py"] # расширения которые не переименовываем, чтоб не подломать пока тестирую
    p = Path(Path().cwd())
    i = 0
    for obj in p.iterdir():
        if obj.is_file():
            if obj.name.split('.')[-1] == extension:
                if extension not in no_rename_extension:
                    Path(obj).rename(f'{new_name}_{obj.name.split()[0][old_name[0]:old_name[1]]}{str(i).zfill(num)}.{extension_new}')
                    i += 1
                else:
                    print(f'{extension} - запрещено к переименованию')


if __name__ == '__main__':
    rename_group("itog", 5, "doc", "txt", [0,3])