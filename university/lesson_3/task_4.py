# 1. Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не
# останется пустым

# 2. ** Как сделать это же задание со строкой: напишите цикл, который выводит на экран и
# «удаляет» первый символ строки, пока она не станет пустой?

# 3. Напишите цикл, который выводит на экран и удаляет элементы списка от самого
# маленького до самого большого, пока он не останется пустым.


l = [1, 2, 5, 6, 7, 5, 9, 8, 7]

while l:
    l.pop()
    print(l)


l = [3, 2, 6, 5, 8, 9, 1]
ll = sorted(l)

while ll:
    ll.pop()
    print(ll)