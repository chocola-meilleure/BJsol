n,m=map(int, input().split())
board=[]
result=[]

for i in range(n):
    board.append(input())

B = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]
    
W = ["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW",]
    
    
min_cnt = []
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = 0
        #위 두 반복문을 통해 탐색의 시작점을 정한다. 
    
        for l in range(8):
            for k in range(8):
        #8*8만큼 w 또는 b 배열과 비교하며 다른 원소의 개수를 센다.
                if board[i+l][j+k] != W[l][k]:
                    cnt+=1

        min_cnt.append(cnt)
        cnt = 0
        for l in range(8):
            for k in range(8):
        #8*8만큼 w 또는 b 배열과 비교하며 다른 원소의 개수를 센다.
                if board[i+l][j+k] != B[l][k]:
                    cnt+=1
                        
        min_cnt.append(cnt)          

print(min(min_cnt))