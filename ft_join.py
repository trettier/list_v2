def ft_join(a, sep=" "):
    c = ''
    d = 0
    for i in a:
        d += 1
    for i in range(d):
        c += str(a[i])
        if i != d - 1:
            c += sep
    return c
