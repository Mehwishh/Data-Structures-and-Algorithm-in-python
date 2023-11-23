# when Array is unsorted 
array= [14,6,7,68,0]
print(f"before sorting : {array}")
n=len(array)
for i in range(n):
    #keep track of sort
    swapped = False
    #print valueof i for each iteration
    print(f"i={i}")  
    for j in range(n-1-i):
        #print value of j for each iteration
        print(f"j={j}") 
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
            swapped = True
    # no swapping means the array is already sorted
    if not swapped:
        break
print(f"after sorting: {array}")


