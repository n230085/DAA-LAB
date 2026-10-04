# Merge Sort
num = int(input("Enter the number of elements: "))
arr = []

#Taking input from the user
for i in range(num):
    arr.append(int(input(f"Enter position {i}: ")))

def merge_sort(arr):
    if len(arr)>1:  #Checking if arr has more than 1 ele
        midArr = len(arr)//2  #finding the mid of arr to divide it into 2 halfs
        leftArr = arr[:midArr]
        rightArr = arr[midArr:]

        merge_sort(leftArr) #Recursively sorting the left half
        merge_sort(rightArr) #Recursively sorting the right half

        i=j=k=0
        while(i<len(leftArr) and j<len(rightArr)):
            if(leftArr[i]<rightArr[j]):
                arr[k] = leftArr[i]
                i+=1
            else:
                arr[k] = rightArr[j]
                j+=1
            k+=1

        while(i<len(leftArr)):
            arr[k] = leftArr[i]
            i+=1
            k+=1

        while(j<len(rightArr)):
            arr[k] = rightArr[j]
            j+=1
            k+=1

merge_sort(arr)
print("The Sorted list is: ",arr)