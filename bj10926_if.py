nums=list(map(int,input().split(" ")))
nums=sorted(nums)

if nums[0]==nums[1]:
    if nums[1]==nums[2]:
        print(10000+nums[0]*1000)
    else: #0=1인데 1!=2인경우 
        print(1000+nums[0]*100)
elif nums[1]==nums[2]: #0!=1이고 1=2인 경우
    print(1000+nums[1]*100)
else:
    print(nums[2]*100)