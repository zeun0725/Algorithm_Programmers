# https://programmers.co.kr/learn/courses/30/lessons/42626
# 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    # 힙정렬 이용
    s_heap = []
    for s in scoville:
        heapq.heappush(s_heap, s)

    while len(s_heap) > 1:
        if s_heap[0] >= K:
            return answer
        min_s = heapq.heappop(s_heap)
        min2_s = heapq.heappop(s_heap)
        heapq.heappush(s_heap, min_s + (min2_s * 2))
        answer += 1

    # length=1로 마지막까지 비교된 스코빌 지수가 K보다 큰지 한번 더 비교
    return answer if s_heap[0] >= K else -1