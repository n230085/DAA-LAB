def heapify(arr,n,i):
    parent=i
    leftChild=2*i+1
    rightChild=2*i+2
    
    if leftChild < n and arr[parent] < arr[leftChild]:
        parent = leftChild
    
    if rightChild < n and arr[parent] < arr[rightChild]:
        parent = rightChild
    
    if parent!=i:
        arr[i],arr[parent] = arr[parent],arr[i]
        heapify(arr,n,parent)


def heap_sort(arr):
    n= len(arr)
    #Step-1 heapify the arr using the max-heap
    for i in range((n//2)-1,-1,-1):
        heapify(arr,n,i)
    
    #Step-2 Extract the element one by one from the heap
    for i in range((n-1),0,-1):
        #Move current root (maximum) to the end of the array
        arr[0],arr[i] = arr[i],a[0]
        #Call heapify of the reduced  heap (size=1)
        heapify(arr,i,0)
        
data=[]
n= int(input("Enter the no.of element in the array:"))
for i in range(n):
    data.append(int(input(f"Enter the {i} position:")))
print("Original array:",data)
heap_sort(data)
print("Sorted array:", data)