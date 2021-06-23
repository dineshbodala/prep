def insertionsort():
    for i in range(1,len(x)):
        c=x[i]
        j=i
        while x[j-1]>c and j>0:
            x[j]=x[j-1]
            j=j-1
        x[j]=c

    return x
