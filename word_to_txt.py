import docx
import glob
import os
import re


def latinic_to_cyrilic(s):
    r = {
        'e': 'е',
        'i': 'і',
        'o': 'о',
        'p': 'р',
        'a': 'а',
        'c': 'с',
        'x': 'х',
        'E': 'У',
        'T': 'Т',
        'I': 'І',
        'O': 'О',
        'P': 'Р',
        'A': 'А',
        'H': 'Н',
        'K': 'К',
        'X': 'Х',
        'C': 'С',
        'B': 'В',
        'M': 'М',
    }
    for k, v in r.items():
        s = s.replace(k, v)

    return s


path = 'docx/'
path_txt = 'new_txt/'

f_error = [f for f in glob.glob(path + "**/*.doc", recursive=True)]

if len(f_error) > 0:
    print("Стара версія наступних файлів:")
    for f in f_error:
        print(f)
    print("Збережіть ці файли в новому форматі та повторіть конвертацію.")
    exit(-1)

files = [f for f in glob.glob(path + "**/*.docx", recursive=True)]

# створення папки для нових файлів
if not os.path.exists("./" + path_txt):
    try:
        os.mkdir("./" + path_txt)
    except OSError:
        print("Помилка створення папки %і failed", path_txt)
        exit(-1)
    else:
        print("Папка %s успішно створена", path_txt)

for f in files:
    print(f, "-->", path_txt[:-1] + f.replace(path[:-1], '') + "txt")
    doc = docx.Document(f)
    s = ''
    for p in doc.paragraphs:
        if len(p.text) > 0:
            p1 = re.sub(r'\s+', ' ', p.text)  # Видалення подвійних пробілів
            s += p1 + '\n'
    s = latinic_to_cyrilic(s)

    file = open(path_txt[:-1] + f.replace(path[:-1], '') + "txt", "w", encoding='utf-8')
    file.writelines(s)
    file.close()
