def ft_join(a, sep=" "):
    c = ''
    for i in a:
        c += str(i)
        c += sep
    for i in sep:
        c = c[:-1]
    return c
