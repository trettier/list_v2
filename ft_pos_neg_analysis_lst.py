def minn(a):
    c = a[0]
    for i in a:
        if i < c:
            c = i
    return (c)


def maxx(a):
    c = a[0]
    for i in a:
        if i > c:
            c = i
    return (c)


def ft_pos_neg_analysis_lst(a):
    b = []
    d = []
    sum1 = 0
    sum2 = 0
    x = 0
    y = 0
    c = 0
    for i in a:
        if i > 0:
            b.append(i)
            sum1 += i
            x += 1
        elif i < 0:
            d.append(i)
            sum2 += i
            y += 1
        else:
            c += 1
    print(f"Положительные:\tОтрицательные:\n"
          f"Количество чисел: {x},\tКоличество чисел: {y},\n"
          f"Максимальная цифра: {maxx(b)},\tМаксимальная цифра: {maxx(d)},\n"
          f"Минимальная цифра: {minn(b)},\tМинимальная цифра: {minn(d)},\n"
          f"Сумма чисел: {sum1},\tСумма чисел: {sum2},\n"
          f"Среднее значение: {sum1 / x}\tСреднее значение: {sum2 / y}\n\n"
          f"Количество нулей: {c}")


ft_pos_neg_analysis_lst([-1, -2, 3, 6, 0])