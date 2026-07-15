n = int (input("Enter number of values:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter value {i+1}:")))
    
for i in range(1,n):
    key=arr[i]
    j=i-1
    
    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j=j-1
    arr[j+1] = key
print("The sorted data is :" , arr)