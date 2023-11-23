# Unsorted Array(WORSE CASE)
array= [1,4,9,0,8,5,33,5,6,78,90,54,1000,199]
print(f"unsorted array: {array}")
n=len(array)
for i in range(n-1):
    #print(f"i={i}")  print valueof i for each iteration
    for j in range(n-1-i):
        #print(f"j={j}") print value of j for each iteration
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
print(f"sorted array: {array}")


# when Array sorted in accending order(BEST CASE)
array= [0,1,2,4]
print(f"before sorting : {array}")
n=len(array)
for i in range(n-1):
    #print valueof i for each iteration
    #print(f"i={i}")  
    for j in range(n-1-i):
        #print value of j for each iteration
        #print(f"j={j}") 
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
print(f"after sorting: {array}")


# when Array sorted in decending order(WORSE CASE)
array= [9,8,7,6]
print(f"before sorting : {array}")
n=len(array)
for i in range(n-1):
    #print valueof i for each iteration
    print(f"i={i}")  
    for j in range(n-1-i):
        #print value of j for each iteration
        print(f"j={j}") 
        if array[j]>array[j+1]:
            temp=array[j]
            array[j]=array[j+1]
            array[j+1]=temp
print(f"after sorting: {array}")

# this algorithm is dumb algrorihm