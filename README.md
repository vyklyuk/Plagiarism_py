# Plagiarism
# Програма перевірки на плагіат скриптів на Python

## Для роботи програми треба:
1. Створити папки 
  - ***DataBase*** - Містить попередні (еталонні) файли для перевірки (на початку може бути порожня)
  - ***New_files*** - Нові файли для перевірки
2. В кожній з цих папок треба створити папки для лабораторок, наприклад ***Lab1***
3. В папку ***New_files/Lab1*** залити файли для перевірки ***(*.py)***
4. У файлі ***plagiarism.py*** задати папку яка перевіряється на плагіат - атрибут ***folder = 'Lab1'***
5. Запістити ***plagiarism.py***
6. В результаті роботи створяться папки:
  - ***New_txt*** - текстові файли готові для перевірки, які потім можна злити в папку DataBase
  - ***Results*** - результати на перевірку плагіату