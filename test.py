from difflib import SequenceMatcher
import glob
import os

SIZE_PLAG = 500
path_res = "Results"


def Find_Matches(text_test, fn_db):
    f_db = open(fn_db, encoding='utf-8', errors='ignore')
    text_db = f_db.read()
    f_db.close()
    # for s in file_1.readlines():
    #     print (s)
    similarity_ratio = SequenceMatcher(None, text_test, text_db).get_matching_blocks()
    # similarity_ratio = SequenceMatcher(None, file1_data, file2_data).ratio()
    # print (similarity_ratio)  #plagiarism detected
    res = ""
    plag = False
    ch = set()
    for s_r in similarity_ratio:
        if s_r[-1] >= SIZE_PLAG:
            if plag == False:
                plag = True
                res = "\n" + fn_db + ":\n"
            m = text_test[s_r[0]:s_r[0] + 50] + " ... " + text_test[s_r[0] + s_r[2] - 10:s_r[0] + s_r[2]]
            m = m.replace("\n", " ")
            res += "Плагіат: " + str(s_r[-1] * 100 // len(text_test)) + "%; " \
                    "Символів: " + str(s_r[-1]) + "; " + \
                    "Текст: " + m + "\n"
            ch = ch.union(set(range(s_r[0], s_r[0] + s_r[2])))
    pr = len(ch) * 100 // len(text_test)
    if plag:
        res += "Сумарний плагіат: " + str(pr) + "%\n"
    return res, ch


# створення папки для нових файлів
if not os.path.exists("./" + path_res):
    try:
        os.mkdir("./" + path_res)
    except OSError:
        print("Помилка створення папки %і failed", path_res)
        exit(-1)
    else:
        print("Папка %s успішно створена", path_res)

path_DataBase = 'DataBase/'
path_test = 'new_txt/'
files_DB = [f for f in glob.glob(path_DataBase + "**/*.txt", recursive=True)]
files_test = [f for f in glob.glob(path_test + "**/*.txt", recursive=True)]

len_DB = len(files_DB)
for f_t in files_test:
    f_test = open(f_t, encoding='utf-8', errors='ignore')
    text_test = f_test.read()
    f_test.close()
    print(f_t)
    res_plag = f_t + "\n"
    ch_plag = set()
    res_plag_memo = ""
    for i, f_DB in enumerate(files_DB):
        print("\r", "Перевірено на:", i * 100 // len_DB, "%", "Звіряю з:", f_DB,
        '                   ', end='')
        res, ch = Find_Matches(text_test, f_DB)
        ch_plag = ch_plag.union(ch)
        res_plag_memo += res

    pr = len(ch_plag) * 100 // len(text_test)
    res_plag += "Плагіат: " + str(pr) + "%\n"
    res_plag += "Унікальність: " + str(100 - pr) + "%\n\n"

    res_plag += res_plag_memo
    print("\r", "Перевірено на: 100%")
    file = open(path_res + f_t.replace(path_test, '/'), "w", encoding='utf-8')
    file.writelines(res_plag)
    file.close()
