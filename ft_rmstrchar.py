def ft_rmstrspc(a, b, c=""):
    n = 0
    for i in a:
        n += 1
    n1 = 0
    for i in b:
        n1 += 1
    d = ""
    for i in range(n):
        d += a[i]
        if b in d:
            d1 = ""
            n2 = 0
            for j in d:
                n2 += 1
            for j in range(n2 - n1):
                d1 += d[j]
            d = d1 + c
    return d


print(ft_rmstrspc("ftthree_sttr", "tt"))