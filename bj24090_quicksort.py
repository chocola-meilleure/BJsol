def quick_sort(arr):
    if len(arr)<2:
        return arr
    
    pivot=arr[0]
    nums = arr[1:]
    less=[]
    greater=[]
    for num in nums:
        if num<pivot:
            less.append(num)
        else:
            greater.append(num)
        
    return quick_sort(less)+[pivot]+quick_sort(greater)

#a,b=map(int,input().split())

inputs = list(map(int,input().split()))
print(quick_sort(inputs))