lst = ['a', 'b', 'c']
lst += 'd' # Работает, строка преобразуется в массив и добавляется к существующему массиву
print(lst)

lst = lst + 'd' # Ошибка, т.к невозможно сложить строку и массив
print(lst)

lst += 42
print(lst) # Ошибка, число не преобразуется в массив, т.к. нет встроенной функции