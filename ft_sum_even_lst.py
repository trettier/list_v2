def ft_sum_even_lst(a):
    j = -1
    c = 0
    for i in a:
        if j == 0:
            j -= 1

        else:
            c += i
            j += 1
    return c
