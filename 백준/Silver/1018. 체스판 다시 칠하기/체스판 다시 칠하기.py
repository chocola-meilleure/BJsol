n, m = map(int,input().split())

wboard = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]

# 입력받은 랜덤칠 보드판
board = [input() for _ in range(n)]

# 최소 덧칠 횟수 -> 최대 덧칠 가능 횟수로 초기화
cnt_min = 64

# j는 행의 시작위치, i는 열의 시작위치 
for j in range(n-8+1):
    for i in range(m-8+1):
        # 덧칠 횟수 초기화
        count = 0

        # 8*8 크기로 잘라 비교
        for row in range(8):
            for col in range(8):
                if board[j + row][i + col] != wboard[row][col]:
                    count += 1

        # 덧칠 횟수가 더 작은 것을 선택
        cnt_min = min(cnt_min, count, 64-count)

print(cnt_min)