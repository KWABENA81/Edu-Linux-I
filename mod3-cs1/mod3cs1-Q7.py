def nfactor(num):
    nf = 1
    if num > 1:
        nf = num * nfactor(num - 1)
    return nf


print(nfactor(5))
