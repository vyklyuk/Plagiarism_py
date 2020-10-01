from pre_proc_txt import create_txt
from test import test

folder = 'Lab1'

path = 'new_files/' + folder
path_txt = 'new_txt/' + folder

SIZE_PLAG = 10
path_res = "Results/" + folder
path_DataBase = 'DataBase/' + folder


create_txt(path, path_txt)
test(path_txt, path_res, path_DataBase, SIZE_PLAG)