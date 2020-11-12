def ft_odd_even_separator_lst(a):
    c = []
    d = []
    for i in a:
        if type(i) == int:
            if i % 2 == 0:
                c.append(i)
            else:
                d.append(i)
    return [c, d]
