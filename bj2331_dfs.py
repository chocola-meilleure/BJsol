n,m = map(int,input().split())
result = [n]
s=str(n) #자릿수 숫자를 구하고 인덱싱하기 위해 str로 바꿔준다. 계산 시 int로 바꾸어 사용한다. 

def cal(number):
    res = 0 
    res+=int(number[-1])**m
    
    for i in range(0,len(number)-1): 
        res+=int(number[i])**m 

    if res in result:
        idx = result.index(res)
        del result[idx:]
        print(result)
        return 0
    else:
        result.append(res)
        cal(str(res))

cal(s)


