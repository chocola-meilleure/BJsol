n=int(input())
sum = 0 
board = list()

for i in range(100):
    board.append([0]*100)


for i in range(n):
    x,y = map(int,input().split())
    for k in range(10):
        for l in range(10):
            board[x-1+k][y-1+l] = 1


for i in range(100):
    for j in range(100):
        sum += board[i][j]

print(sum)
