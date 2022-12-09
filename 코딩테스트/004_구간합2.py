"""
004 구간 합 구하기2
시간 제한 : 1초
난이도 : 실버1
백준 11660번
"""

# N, q = map(int, input().split())
# array = []
# for _ in range(N):
#     array.append(list(map(int, input().split())))

# print(array)
N = 4
q = 3
array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

x1 = 2
y1 = 2
x2 = 3
y2 = 4

prefix_arr = [0] * (N+1)
