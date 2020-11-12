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


def ft_odd_even_analysis_lst(a):
    b = []
    d = []
    sum1 = 0
    sum2 = 0
    x = 0
    y = 0
    for i in a:
        if i % 2 == 0:
            b.append(i)
            sum1 += i
            x += 1
        else:
            d.append(i)
            sum2 += i
            y += 1
    print("Анализ списка:")
    print(f"Количество четных чисел: {x},\t\tКоличество нечетных чисел: {y}")
    print(f"Максимальная четная цифра: {maxx(b)},\t\tМаксимальная нечетная цифра: {maxx(d)},")
    print(f"Минимальная четная цифра: {minn(b)},\t\tМинимальная нечетная цифра: {minn(d)},")
    print(f"Сумма четных чисел: {sum1},\t\tСумма нечетных чисел: {sum2},")
