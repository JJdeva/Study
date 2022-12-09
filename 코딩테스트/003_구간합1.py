"""
003 구간 합 구하기1
시간 제한 : 0.5초
난이도 : 실버3
백준 11659번
"""

N, M = map(int, input().split())
numlist = list(map(int, input().split()))

# 합 배열
s = [numlist[0]]
for i in range(N-1):
    s.append(s[i]+numlist[i+1])

# 답을 담을 리스트
answer = []
for _ in range(M):
    i, j = map(int, input().split())
    # 1 -> S[0] , 2 -> S[1]
    if i == 1:
        answer.append(s[j-1])
    else:
        answer.append(s[j-1] - s[i-2])

for i in answer:
    print(i)


# 해답지
N, M = map(int, input().split())
numlist = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numlist:
    temp = temp + i
    prefix_sum.append(temp)

for i in range(M):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum(s-1))