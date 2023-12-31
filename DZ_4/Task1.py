"""
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами).
"""


def pearson_correlation(x, y):
    assert len(x) == len(y), 'Длины массивов должны быть равны'

    # Рассчитаем средние значения
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Рассчитаем квадратные отклонения
    sq_diff_x = sum((xi - mean_x) ** 2 for xi in x)
    sq_diff_y = sum((yi - mean_y) ** 2 for yi in y)

    # Рассчитаем корреляцию
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    corr = numerator / ((sq_diff_x ** 0.5) * (sq_diff_y ** 0.5))

    return corr


# Пример использования
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
pc = pearson_correlation(x, y)
print(f'Значение корелляции Пирсона между двумя наборами данных = {pc}')  # 0.9999999999999998
