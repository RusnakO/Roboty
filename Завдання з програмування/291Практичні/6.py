def frac(n, m):
    numerator = n
    denominator = m
    #знаходимо НСД чисельника та знаменника:
    if n == 0:
        nsd = m
    while m != 0:
        if n > m:
            n = n - m
        else:
            m = m - n
    nsd = n
    return (numerator // nsd, denominator // nsd)
    
