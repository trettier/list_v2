def ft_odd_even_separator_lst(a):
    c = [[], []]
    for i in a:
        if type(i) == int:
            if i % 2 == 0:
                c[0].append(i)
            else:
                c[1].append(i)
    return c
