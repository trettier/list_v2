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
