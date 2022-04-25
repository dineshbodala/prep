def rec(x):
    if x==1:
        return 1
    else:
        return x*rec(x-1)
print(rec(7))
