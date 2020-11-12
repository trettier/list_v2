def ft_pos_neg_separator_lst(a):
    b = []
    c = []
    d = []
    for i in a:
        if i < 0:
            b.append(i)
        elif i > 0:
            d.append(i)
        else:
            c.append(i)
    return [b, c, d]
