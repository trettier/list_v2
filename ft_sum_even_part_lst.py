def ft_sum_even_part_lst(a):
    c = 0
    for i in a:
        if type(i) == int:
            if i % 2 == 0:
                c += i
    return c
