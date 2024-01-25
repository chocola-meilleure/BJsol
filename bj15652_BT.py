n,m = map(int,input().split())
combination = []

def dfs(cnt, index):
    #멈출조건
    if cnt-1 == m:
        print(' '.join(map(str,combination)))
        return 

    #탐색조건
    for i in range(index,n+1):
        combination.append(i)
        dfs(cnt+1,i)
        combination.pop()
