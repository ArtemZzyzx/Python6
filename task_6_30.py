# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstNumber = int(input('Введите первый элемент: '))
step = int(input('Введите шаг: '))
count = int(input('Введите количество: '))
print(*[i for i in range(firstNumber, firstNumber + (count - 1) * step + 1, step)])