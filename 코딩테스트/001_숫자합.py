"""
001 숫자의 합 구하기
시간 제한 : 1초
난이도 : 브론즈4
백준 11720번
"""

N = int(input())
num = input()

cnt = 0
for i in num:
    cnt += int(i)

print(cnt)