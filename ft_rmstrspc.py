def ft_join(a, sep=" "):
    c = ''
    for i in a:
        c += str(i)
        c += sep
    for i in sep:
        c = c[:-1]
    return c


def ft_strtlist(a):
    j = 0
    c = [""]
    t = False
    for i in a:
        if i != " ":
            c[j] += i
            t = True
        elif t:
            j += 1
            t = False
            c.append("")
    if c[-1] == '':
        c.pop()
    return c


def ft_rmstrspc(str):
    a = ft_join(ft_strtlist(str), '')
    return a
