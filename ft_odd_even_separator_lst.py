def ft_odd_even_separator_lst(a):
    b = []
    c = []
    d = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
        else:
            c.append(i)
    d.append(b)
    d.append(c)
    return d
