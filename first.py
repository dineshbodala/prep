def binary_search(x,n):
    l=0
    r=len(x)-1
    while l<r:
        mid=int((l+r)/2)
        if x[mid]==n:
            return mid
            break
        elif x[mid]<n:
            l=mid
        else:
            r=mid
    return -1

def selection_sort():
	for i in range(len(x)-1):
		min=i
		for j in range(i,len(x)):
			if x[j]<x[min]:
				x[min]=x[j]
		x[min],x[i]=x[i],x[min]
	return x
	
	#comment
