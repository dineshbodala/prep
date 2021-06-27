def binary_search(x,n):
    l=0
    r=len(x)
    while l<r:
        mid=int((l+r)/2)
        if x[mid]==n:
            return mid
            break
        elif x[mid]<n:
            l=mid+1
        else:
            r=mid-1
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
x=[1,2,3,4,5]
n=5
print(binary_search(x,n))
