def heapify(arr,n,i):
    """
    Sifts down the element at index i to maintain the Max-Heap property.
    n: active size of the heap
    i: index of the current node
    """
    parent = i
    leftChild = 2*i+1
    rightChild = 2*i+2

    if leftChild < n and arr[leftChild] > arr[parent]:
        parent = leftChild
    if rightChild < n and arr[rightChild] > arr[parent]:
        parent = rightChild

    if parent != i:
        arr[i],arr[parent] = arr[parent],arr[i]
        heapify(arr,n,parent)

def heapSort(arr):
    n = len(arr)
    #Step-1 Heapify the arr using MaxHeap
    for i in range((n//2) - 1,-1,-1):
        heapify(arr,n,i)

    # Step 2: Extract elements one by one from the heap
    for i in range((n-1),0,-1):
        # Move current root (maximum) to the end of the array
        arr[0],arr[i] = arr[i],arr[0]
        # Call heapify on the reduced heap (size = i)
        heapify(arr,i,0)

data=[]
n=int(input("Enter the No.of values in array: "))
for i in range(n):
    data.append(int(input(f"Enter the {i} position: ")))

print("original array: ",data)
heapSort(data)
print("Sorted array: ",data)