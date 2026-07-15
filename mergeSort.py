num = int(input("Enter your number of elements:"))

arr =[]

for i in range(num):
    n = int(input (f"Enter element {i+1}:"))
    arr.append(n)

def merge_sort(arr):
    if len(arr)>1:
        mid_arr = len(arr)//2
        left_arr = arr[:mid_arr]
        right_arr = arr[mid_arr:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
    
        i=j=k=0
        while (i<len(left_arr) and j<len(right_arr)):
            if(left_arr[i]<right_arr[j]):
                arr[k] =left_arr[i]
                i+=1
            else:
                arr[k]= right_arr[j]
                j+=1
            k+=1
        
        while(i<len(left_arr)):
            arr[k]= left_arr[i]
            i+=1
            k+=1
        while(j<len(right_arr)):
            arr[k]=right_arr[j]
            j+=1
            k+=1
            
merge_sort(arr)
print("The sorted list is :",arr)
            