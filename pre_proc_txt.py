
import glob
import re
import my_save

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


# f_error = [f for f in glob.glob(path + "**/*.doc", recursive=True)]
#
# if len(f_error) > 0:
#     print("Стара версія наступних файлів:")
#     for f in f_error:
#         print(f)
#     print("Збережіть ці файли в новому форматі та повторіть конвертацію.")
#     exit(-1)

def create_txt(path, path_txt):

    files = [f for f in glob.glob(path + "/**/*.py", recursive=True)]
    for f in files:
        f_txt = path_txt[:-1] + f.replace(path[:-1], '') + ".txt"
        f_dir = f_txt[:f_txt.rfind("/")]
        print(f, "-->", f_txt)
        # print(f_dir)
        f_db = open(f, encoding='utf-8', errors='ignore')
        text_db = f_db.read()
        f_db.close()
        text_db = text_db.split('\n')
        s = ''
        for p in text_db:
            if len(p) > 0:
                p1 = re.sub(r'\s+', ' ', p)  # Видалення подвійних пробілів
                s += p1 + '\n'
        s = latinic_to_cyrilic(s)

        my_save.save_txt(f_txt, s)