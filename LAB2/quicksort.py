#quick sort
num = int(input("Enter the number of ele: "))

arr = []
for i in range(num):
    arr.append(int(input(f"Enter ele {i}: ")))

def partion(arr,low,high):
    pivot = arr[high] 
    i=low-1
    for j in range(low,high):
        if arr[j]<= pivot :
            i+=1
            arr[j],arr[i] = arr[i],arr[j]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if(low<high):
        pivot = partion(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

quick_sort(arr,0,num-1)
print(f"Sorted array is {arr}")