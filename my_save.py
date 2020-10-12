import os

def save_txt(file_name, text):
    txt_dir = file_name.split('/')

    # створення папки для нових файлів
    for i, d in enumerate(txt_dir[:-1]):
        mkd = "/".join(txt_dir[:i+1])
        if not os.path.exists("./" + mkd):
            try:
                os.mkdir("./" + mkd)
            except OSError:
                print("Помилка створення папки {0} ".format(mkd))
                exit(-1)
            else:
                print("Папка {0} успішно створена".format(mkd))

    file = open(file_name, "w", encoding='utf-8')
    file.writelines(text)
    file.close()