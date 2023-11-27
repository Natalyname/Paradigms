"""
# Процедурное программирование в декларативном стиле
# для возможности переиспользования процедурного кода в других проектах.

Таблица умножения.
На вход подается число n.
   Задача:
Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм.
"""


def print_multiplication_table(n: int = 10, cols: int = 8) -> None:
    s, e = 1, n if n <= cols else cols  
    while True:
        offset = len(str(e * e))  
        matrix = ((a * b for a in range(s, e + 1)) for b in range(1, n + 1))
        for row_i, row in enumerate(matrix, 1):
            for item_i, item in enumerate(row, s):
                print(f'{str(row_i).rjust(offset)} *{str(item_i).rjust(offset)} =', end='')
                print(str(item).rjust(offset+1), end='  ')
            print()
        if e == n:
            break
        s, e = s + cols, e + cols if e + cols <= n else n
        print()


if __name__ == '__main__':
    print_multiplication_table(10, 5)
