from heapq import heappush, heappop
import sys

# 입력 받기
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))

# 우선순위 큐 초기화
pq = []
for i, elem1 in enumerate(arr1):
    # (합, A의 인덱스, B의 인덱스)로 큐에 추가
    heappush(pq, (elem1 + arr2[0], i, 0))

# K번째까지 반복
while pq and k > 0:
    v, i, j = heappop(pq)
    k -= 1
    # K번째 원소를 찾으면 종료
    if k == 0:
        print(v)
        break
    # B의 다음 원소가 있다면, 현재 A의 원소와 B의 다음 원소를 합한 새로운 쌍을 큐에 추가
    if j + 1 < m:
        heappush(pq, (arr1[i] + arr2[j + 1], i, j + 1))