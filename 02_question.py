"""
Задача 6.
Дана строка (возможно, пустая), состоящая из буквы A-Z:

AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
BBBBBBBBBBBBBBBBBBBBBBB

Вам нужно написать RLE
функция, которая выведет следующую строку:

A4B3C2XYZD4E3F3A6B28

И это будет генерировать ошибку, если недопустимая строка
принимается как ввод.

Пояснения: если символ встречается 1 раз,
он остается неизменным; Если символ
повторяется более 1 раза,
к ней добавляется количество повторений.

"""

text = input("Enter text: ")

current_char = text[0]
new_txt = ''
counter = 0
for i in range(0, len(text)):
    char = text[i]
    if current_char == char:
        counter += 1
    else:
        new_txt += current_char
        if counter > 1:
            new_txt += str(counter)
        current_char = char
        counter = 1

    if i == len(text) - 1:
        new_txt += char
        if counter > 1:
            new_txt += str(counter)

print(new_txt)
