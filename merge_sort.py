def merge_sort(x):
    if len(x)>1:


        mid=len(x) // 2
        left=x[:mid]
        right=x[mid:]

        merge_sort(left)

        merge_sort(right)

        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                x[k]=left[i]
                i+=1

            else:
                x[k]=right[j]
                j+=1

            k+=1

        while i<len(left):
            x[k]=left[i]
            i+=1
            k+=1

        while j<len(left):
            x[k]=right[j]
            j+=1
            k+=1

        return x

x=[2,1,4,7,9,8]
print(merge_sort(x))






