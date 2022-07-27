def maxheapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[largest] < arr[left]:
        largest=left

    if right<n and arr[largest] < arr[right]:
        largest=right

    if largest!=i:
        arr[i], arr[largest]=arr[largest], arr[i]

        maxheapify(arr,n,largest)

array=[222,6,12,132,4,213,3453,56,12,2,55,67,97,2,122,5,6,232,89]
n=len(array)

def heapsort(arrays):
    for i in range (n-1,0,-1):
        arrays[i],arrays[0] = arrays[0],arrays[i]
        maxheapify(arrays,i,0)
for i in range ((n//2)-1,-1,-1):
    maxheapify(array,n,i)


heapsort(array)

print("Max sorted heap is")
for i in range(n):
    print (array[i])
