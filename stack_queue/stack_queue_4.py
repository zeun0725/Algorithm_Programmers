# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
import heapq
def solution(priorities, location):
    answer = 0

    #최대힙 구현
    heap = [-idx for idx in priorities]
    heapq.heapify(heap)

    #큐 구현 (시간복잡도 1을 위함)
    _queue = list(zip(priorities, [idx for idx in range(len(priorities))]))
    queue = deque(_queue)

    #큐의 맨 앞의 값이 최대값이고 우리가 찾는 location이면 while문을 멈춘다
    while queue:
        value = queue.popleft()
        if abs(heap[0]) == value[0]:
            heapq.heappop(heap)
            answer += 1
            if value[1] == location:
                break
        else:
            queue.append(value)
    return answer

solution([1, 1, 9, 1, 1, 1], 0)