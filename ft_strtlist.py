def ft_strtlist(a):
    j = 0
    c = [""]
    t = False
    ln = 0
    for i in a:
        if i != " ":
            c[j] += i
            t = True
        elif t:
            j += 1
            t = False
            c.append("")
    for i in c:
        ln += 1
    if c[-1] == '':
        fin = ""
        for i in range(ln - 1):
            fin += i
        return fin
    return c