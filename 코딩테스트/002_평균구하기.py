"""
002 평균 구하기
시간 제한 : 2초
난이도 : 브론즈1
백준 1546번
"""

# N : 시험을 본 과목의 개수
N = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)
print(100*sum(arr)/max_num/N)