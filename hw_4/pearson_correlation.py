import math


def pearson_correlation(list_1, list_2):
    # Проверка, одинаковой ли длины списки
    if len(list_1) != len(list_2):
        raise ValueError("Списки должны быть одинаковой длины")

    n = len(list_1)

    # Расчет среднего значения
    mean_x = sum(list_1) / n
    mean_y = sum(list_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in list_1]) / float(len(list_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in list_2]) / float(len(list_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(list_1, list_2)]) / float(len(list_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


if __name__ == '__main__':
    list_1 = [10, 22, 33, 14, 25, 37, 7]
    list_2 = [16, 27, 38, 19, 25, 16, 17]

    correlation = round(pearson_correlation(list_1, list_2), 3)
    print(f"Корреляция Пирсона: {correlation}")