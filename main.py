import matplotlib.pyplot as plt
import math


def divided_into_classes(data_x, data_y):
    class_1 = []
    class_2 = []

    for a, b in zip(data_x, data_y):
        if b == 1:
            class_1.append(a)
        if b == -1:
            class_2.append(a)

    return class_1, class_2


def calculate_mu(x_n):
    sum_x = 0
    for i in x_n:
        sum_x += i

    return sum_x / len(x_n)


def div_into_x_y(my_class):
    x_s = []
    for _ in my_class:
        x_s.append(_[0])

    y_s = []
    for _ in my_class:
        y_s.append(_[1])

    return x_s, y_s


def calculate_variance(mu, x_y_s):
    summa = 0

    for i in x_y_s:
        summa += (i - mu) ** 2

    return (1 / (len(x_y_s) - 1)) * summa


def calculate_GaussianNB(x_y_s, mu, variance):
    return 1 / math.sqrt(2 * math.pi * variance) * math.exp(-(x_y_s - mu) ** 2 / (2 * variance))


def define_class(P_x_1, P_y_1, P_x_2, P_y_2, P_C=0.5):
    score_class1 = P_C * P_x_1 * P_y_1
    score_class2 = P_C * P_x_2 * P_y_2

    result = 0
    if score_class1 > score_class2:
        result = 1 # относится к классу '1'
    if score_class2 > score_class1:
        result = -1 # относится к классу '-1'

    return result



if __name__ == "__main__":
    # Вариант 1
    data_x = [(5.8, 2.7), (6.7, 3.1), (5.7, 2.9), (5.5, 2.4), (4.8, 3.4), (5.4, 3.4), (4.8, 3.0), (5.5, 2.5),
              (5.3, 3.7), (7.0, 3.2), (5.6, 2.9), (4.9, 3.1), (4.8, 3.0), (5.0, 2.3), (5.2, 3.4), (5.1, 3.8),
              (5.0, 3.0), (5.0, 3.3), (4.6, 3.1), (5.5, 2.6), (5.0, 3.5), (6.7, 3.0), (6.0, 2.2), (4.8, 3.1),
              (6.4, 2.9), (5.6, 3.0), (4.4, 3.0), (4.9, 2.4), (5.6, 3.0), (5.0, 3.6), (5.1, 3.3), (5.8, 4.0),
              (5.5, 2.4), (5.2, 2.7), (5.1, 3.8), (5.1, 3.5), (5.5, 4.2), (4.9, 3.1), (5.9, 3.2), (5.7, 2.6),
              (4.7, 3.2), (5.4, 3.9), (5.8, 2.6), (5.1, 3.4), (6.4, 3.2), (5.8, 2.7), (5.6, 2.7), (5.7, 2.8),
              (5.4, 3.0), (5.0, 3.2), (4.6, 3.4), (6.0, 2.7), (6.6, 3.0), (4.9, 3.0), (4.9, 3.6), (4.4, 3.2),
              (5.4, 3.4), (6.0, 3.4), (5.9, 3.0), (6.1, 2.8), (5.1, 3.7), (5.5, 3.5), (6.1, 3.0), (6.2, 2.2),
              (5.7, 3.0), (5.2, 3.5), (5.4, 3.7), (4.6, 3.2), (5.2, 4.1), (5.0, 2.0), (6.8, 2.8), (5.0, 3.5),
              (6.7, 3.1), (6.3, 3.3), (6.0, 2.9), (4.7, 3.2), (6.6, 2.9), (5.6, 2.5), (4.4, 2.9), (6.2, 2.9),
              (6.1, 2.9), (4.3, 3.0), (6.9, 3.1), (5.7, 3.8), (5.4, 3.9), (6.1, 2.8), (4.6, 3.6), (5.5, 2.3),
              (4.8, 3.4), (6.5, 2.8), (6.3, 2.5), (5.1, 3.8), (5.7, 4.4), (5.0, 3.4), (4.5, 2.3), (5.7, 2.8),
              (5.1, 2.5), (5.1, 3.5), (6.3, 2.3), (5.0, 3.4)]
    data_y = [1, 1, 1, 1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1,
              -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1,
              -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1,
              -1, -1, -1, -1, 1, 1, -1, 1, -1]


    # my_point = [5.2, 3.1]

    my_points = [
        (5.2, 3.1),  # Точка в центре кластера
        (6.5, 2.9),  # Точка в области класса 1
        (4.9, 3.3),  # Точка в области класса -1
        (5.8, 2.5),  # Точка на границе
        (5.9, 3.6),  # Точка на границе
        (6.3, 2.4),  # Точка в области класса 1
        (4.8, 3.5),  # Точка в области класса -1
        (6.7, 3.3),  # Точка в области класса 1
        (4.5, 3.2),  # Точка в области класса -1
        (6.4, 2.6),  # Точка в области класса 1
    ]


    class1, class2 = divided_into_classes(data_x, data_y)

    x_1, y_1 = div_into_x_y(class1)
    x_2, y_2 = div_into_x_y(class2)

    mu_x_class1 = calculate_mu(x_1)
    mu_y_class1 = calculate_mu(y_1)

    mu_x_class2 = calculate_mu(x_2)
    mu_y_class2 = calculate_mu(y_2)

    var_x_1 = calculate_variance(mu_x_class1, x_1)
    var_y_1 = calculate_variance(mu_y_class1, y_1)

    var_x_2 = calculate_variance(mu_x_class2, x_2)
    var_y_2 = calculate_variance(mu_y_class2, y_2)


    count = 1
    for point in my_points:

        P_x_class1 = calculate_GaussianNB(point[0], mu_x_class1, var_x_1)
        P_y_class1 = calculate_GaussianNB(point[1], mu_y_class1, var_y_1)

        P_x_class2 = calculate_GaussianNB(point[0], mu_x_class2, var_x_2)
        P_y_class2 = calculate_GaussianNB(point[1], mu_y_class2, var_y_2)

        print(f"Точка № {count} {point} относится к классу '{define_class(P_x_class1, P_y_class1, P_x_class2, P_y_class2)}'")
        count += 1




    # P_x_class1 = calculate_GaussianNB(my_point[0], mu_x_class1, var_x_1)
    # P_y_class1 = calculate_GaussianNB(my_point[1], mu_y_class1, var_y_1)
    #
    # P_x_class2 = calculate_GaussianNB(my_point[0], mu_x_class2, var_x_2)
    # P_y_class2 = calculate_GaussianNB(my_point[1], mu_y_class2, var_y_2)
    #
    # define_class(P_x_class1, P_y_class1, P_x_class2, P_y_class2)



    plt.figure(figsize=(8, 8))
    plt.scatter(x_1, y_1, c='blue', marker='^', label='Класс 1', s=50)
    plt.scatter(x_2, y_2, c='red', marker='D', label='Класс -1', s=50)
    # plt.scatter(my_point[0], my_point[1], c='green', label='Моя точка', s=50)

    plt.scatter(my_points[0][0], my_points[0][1], c='green', label='Моя точка №1', s=50)
    plt.scatter(my_points[1][0], my_points[1][1], c='gray', label='Моя точка №2', s=50)
    plt.scatter(my_points[2][0], my_points[2][1], c='black', label='Моя точка №3', s=50)
    plt.scatter(my_points[3][0], my_points[3][1], c='orange', label='Моя точка №4', s=50)
    plt.scatter(my_points[4][0], my_points[4][1], c='yellow', label='Моя точка №5', s=50)
    plt.scatter(my_points[5][0], my_points[5][1], c='lime', label='Моя точка №6', s=50)
    plt.scatter(my_points[6][0], my_points[6][1], c='cyan', label='Моя точка №7', s=50)
    plt.scatter(my_points[7][0], my_points[7][1], c='maroon', label='Моя точка №8', s=50)
    plt.scatter(my_points[8][0], my_points[8][1], c='pink', label='Моя точка №9', s=50)
    plt.scatter(my_points[9][0], my_points[9][1], c='brown', label='Моя точка №10', s=50)

    plt.legend()
    plt.show()


    # print(class1)
    # print(class2)

    # print(mu_x_class1, mu_y_class1)
    # print(mu_x_class2, mu_y_class2)

    # print(var_x_1, var_y_1, var_x_2, var_y_2)

    # print(P_x_class1)
    # print(P_y_class1)

    # print(1/2 * P_x_class1 * P_y_class1)
    # print(1/2 * P_x_class2 * P_y_class2)