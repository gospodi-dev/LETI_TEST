'''
# Функция считывания данных с клавиатуры - input()
name = input("Hello!\n") # всегда возвращает строку
print("Hello, ", name)
# Функция позволяет узнать тип объекта - type()
print(type(100))
name = input()
type_name = type(name)
print(name, type_name)
# Задание - Прочитайте данные пользователя с клавиатуры (не используйте приветственное сообщение!). Выведите на экран строку: "Your data: прочитанные_с_клавиатуры_данные".
a = input()
print("Your data:", a)

# ООП
"""
Важные определения:
- класс (тип) - это типы данных в Python
- объект (экземпляр класса)
- атрибуты: поля (свойства объекта) и методы (действия над объектом)
"""
# Числа
# Задача
"""a = 1000000
type(a)
<class 'int'>
a = (-1.91 - 12j)
type(a)
<class 'complex'>
a = -3.123
type(a)
<class 'float'>
a = 19.2j
type(a)
<class 'complex'>
a = 2E3
type(a)
<class 'float'>
a = 2.1e-4
type(a)
<class 'float'>
a = 0o157
type(a)
<class 'int'>
a = 0x9f
type(a)
<class 'int'>
a = 0b10111
type(a)
<class 'int'>
"""
# Математические операции
+ Сложение
- Вычитание
* Умножение
/ Деление
// Деление с округлением в низ
% Остаток деления
x ** y Возведение в степень


# Строки. Функции и методы строк
# input() - всегда возвращает строку
my_str = 'AQBWCFD'
index = 5
print(my_str[index])
my_str = 'AQBWCFD'
index = -3
print(my_str[index])
# Извлечение срезов
my_str = 'AQBWCFD'
i = 2
j = 7
k = 2
print(my_str[i:j:k]) # извлечение среза. Извлекаются элементы от i до j-1 с шагом k.
# По умолчанию i=0, j - длина строки, k=1
# Извлечение срезов с отрицательным шагом
# При k<0 порядок использования i и j должен быть изменен на противоположный: my_str[j:i:k]
print(my_str[::-1])
# Извлечение срезов с отрицательным шагом
# При k<0 порядок использования i и j должен быть заменен на противоположный: my_str[j:i:k]
'my_str[::-1]'
#'DFCWBQA'
# Операторы сравнения со строками
# Проверка вхождения in и not in 

# Приведение типов : int(), float(), bool(), str()
a = int(input())
print(a)
print(type(a))

# Задача 1-2-2-1. Прочитайте строку с клавиатуры и выведите на экран ее длину.
a = input()
print(len(a))
# Задача 1-2-2-2. Прочитайте строку с клавиатуры и выведите на экран её же, приведенную к верхнему регистру.
a = input()
print(a.upper())
# Задача 1-2-2-3. На вход программе подается строка - объект типа str. Напишите программу, которая заменяет каждый символ 'a' в строке на символ 'o', а каждый символ 'T' на символ 'R' и выводит результат на экран.
a = input()
a = a.replace('a', 'o')
a = a.replace('T', 'R')
print(a)
'''

# СПИСКИ
# список (list) - последовательность упорядоченных разнородных объектов.
# изменяемый объект. Может состоять из произвольного уровня вложенности.
# exemple_list = ['hello', 1, 2, ['world', '!']] 

# Доступ к воженному элементу.
'''example_list = ['hello', 1, 2, ['world', '!']]
print(example_list[0][0])
print(example_list[3][0][2])

# Проверка на равенство
[1, 2] > [2, 1] # False
# Проверка на вхождение
[1] in [1, 2, 3] # False

# Конкатенация - "склеивание списков"
[1, 2] + [3, 4] # [1, 2, 3, 4]

# Дублирование
[1, 2, 3] * 2 # [1, 2, 3, 1, 2, 3]'''

# Методы строк и списков

# 1. Ввести строку S, слова которой разделены точкой с запятой. Посчитайте количество слов в строке. 

'''# Ввожу в программу строку 
s = input("s = ") 
# Трансформирую строку в список слов, разделённых символом ";": s.split(";") 
# Вычисляю длину этого списка: len(...) 
count = len(s.split(";")) 
# Вывожу результат 
print("Количество слов:",count)'''

# 2. Дана строка (вводится с клавиатуры). Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина первой части должна быть на один символ МЕНЬШЕ). Переставьте эти две части местами, результат запишите в новую строку и выведите на экран (используйте срезы и их сложение).

'''# Ввожу строку в программу 
s = input("s = ") 
# Вырезаю из неё подстроку от нулевого символа 
# до середины, если длина нечётная, то вырезаю 
# до середины минус один символ 
s1 = s[:len(s)//2] 
# Вырезаю из строки s подстроку с середины до конца. 
# Если длина строки нечётная, то вырезаю с середины 
# минус один до конца строки 
s2 = s[len(s)//2::] 
# Соединяю вторую и первую строки и записываю в 
# переменную result 
result = s2 + s1 
# Вывожу результат на экран 
print(result)'''

# 3. Дана строка, в которой слова разделены пробелами (вводится с клавиатуры). Вывести все слова этой строки в алфавитном порядке (использовать преобразование в список и сортировку). 

'''# Ввожу строку в программу 
s = input("S = ") 
# Трансформирую строку в список слов 
s = s.split() 
# Сортирую список в алфавитном порядке 
s = sorted(s) 
# Вывожу список на экран 
print(s)'''

# 4. Дана строка, в которой слова разделены пробелами (вводится с  клавиатуры). Найдите в этой строке самое длинное слово.  Выведите на экран это слово и его длину. Если таких слов несколько, то вывести их все.

'''# Ввожу строку в программу 
s = input("S = ") 
# Трансформирую строку в список слов 
s = s.split() 
# Ищу длину самого длинного слова 
# Для начала длиной самого длинного слова считаю ноль 
m = 0 
# Запускаю цикл по всем словам списка 
for w in s: 
    # Если длина текущего слова больше максимальной 
    # длины, то... 
    if len(w) > m: 
        # ... записываю в качестве максимальной длины 
        # длину текущего слова 
        m = len(w) 
# Запускаю цикл по всем словам списка 
for w in s: 
    # Если длина текущего слова равна максимальной 
    # длине, то... 
    if len(w) == m: 
        # ... вывожу на экран текущее слово и его длину 
        print(w,"длина =",m)'''

# Задача 1-2-3-1. Прочитайте список строк с клавиатуры (элементы отделены точкой с запятой) и выведите на экран длину списка.

'''strings = input().split(';')
print('Длина списка строк:', len(strings))'''

lines = input("Введите линии (разделенные точкой с запятой): ")
lines_list = lines.split(";")

print("Количество строк:", len(lines_list))

# Задача 1-2-3-2 Прочитайте список строк, разделенных пробелом, с клавиатуры и создайте на его основе строку с разделителем *. Выведите получившуюся строку на экран.
'''text = input("Введите текст, разделенный пробелами: ").split()
result = "*".join(text)
print(result)'''