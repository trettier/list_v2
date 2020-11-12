def ft_rmstrspc(a):
    b = []
    c = ""
    for i in a:
        b.append(i)
    print(b)
    for j in b:
        if j == " ":
            b.remove(j)
    print(b)
    for o in b:
        c += o
    return c
