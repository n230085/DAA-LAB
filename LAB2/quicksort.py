num = int(input("Enter a number of elements:"))

arr = []
for i in range (num):
    n = int(input(f"Enter Element {i+1}:"))
    arr.append(n)

def pivot(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low, high):
        if(arr[j]<=pivot):
            i+=1 
            arr[j],arr[i]=arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr,low,high):
    if low<high:
        pi=pivot(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
        

quickSort(arr,0,num-1)
print("The Sorted list is:",arr)