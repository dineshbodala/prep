def selectionsort():
    for i in range(len(x)-1):
        min=i
        for j in range(i,len(x)):
            if x[min]>x[j]:
                min=j
        x[min],x[i]=x[i],x[min]
    return x

