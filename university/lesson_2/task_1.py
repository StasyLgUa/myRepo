import math

print("hello, world")

"""
1. Определите является ли строка записью числа. (Подсказка: ищите как это
сделать с помощью методов строк)
"""
q = input()
print(q.isnumeric())
print(q.isdigit())
#print(int(math.isfinite(q)))

"""
2. Посчитайте сколько у вас пробелов в строке. 
"""

print("Amount of spaces is " + str(q.count(" ")))

"""
3. Посчитайте сколько у вас символов точки \".\" в строке.
"""
print("Amount of dots is " + str(q.count(".")))

"""
4. Создайте строку \"Homework\". Преобразуйте ее в строку длиной 100 символов,
посередине которой исходное слово, а с обоих сторон строка заполнена
пробелами. Выведите ее на экран.
"""
my_string = "Homework"
print(my_string.center(100))

"""
5. Сделайте первые буквы слов строки большими (upper case).
"""
print(str(q.title()))
