from difflib import SequenceMatcher
import glob
import my_save
import pandas as pd


def Find_Matches(text_test, fn_db, SIZE_PLAG):
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

def test(path_txt, path_res, path_DataBase, SIZE_PLAG):

    files_DB = [f for f in glob.glob(path_DataBase + "/**/*.txt", recursive=True)]
    files_test = [f for f in glob.glob(path_txt + "/**/*.txt", recursive=True)]

    all_files = files_test + files_DB

    len_DB = len(all_files) - 1
    df = pd.DataFrame(columns=['File', 'Плагіат', 'Унікальність'])
    for f_t in files_test:
        f_test = open(f_t, encoding='utf-8', errors='ignore')
        text_test = f_test.read()
        f_test.close()
        print(f_t)
        res_plag = f_t + "\n"
        ch_plag = set()
        res_plag_memo = ""
        for i, f_DB in enumerate(all_files):
            if f_DB != f_t:
                print("\r", "Перевірено на:", i * 100 // len_DB, "%", "Звіряю з:", f_DB,
                '                   ', end='')
                res, ch = Find_Matches(text_test, f_DB, SIZE_PLAG)
                ch_plag = ch_plag.union(ch)
                res_plag_memo += res

        pr = len(ch_plag) * 100 // len(text_test)
        res_plag += "Плагіат: " + str(pr) + "%\n"
        res_plag += "Унікальність: " + str(100 - pr) + "%\n\n"
        df = df.append({'File': f_t, 'Плагіат': pr, 'Унікальність': 100 - pr}, ignore_index=True)
        res_plag += res_plag_memo
        print("\r", "Перевірено на: 100%")

        my_save.save_txt(path_res + f_t.replace(path_txt, '/'), res_plag)
    df= df.sort_values('Плагіат', ascending=False)
    df.to_excel('Results.xlsx', 'Results', index=False)