import sys
input = sys.stdin.readline
 
n = int(input())
nums = list(map(int, input().split()))  # n개의 수
signs = list(map(int, input().split()))     # n-1개의 연산자
 
max_num = -1e9
min_num = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == n:  # 재귀 종료 조건
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return 

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)
 
dfs(1, nums[0], signs[0], signs[1], signs[2], signs[3])
 
print(max_num)
print(min_num)

