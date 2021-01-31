# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def get_heapq(start, jobs):
    heap = []
    for job in jobs:
        if job[0] < start:
            heapq.heappush(heap, job[::-1])
    return heap


def solution(jobs):
    answer, start = 0, 0
    len_job = jobs.__len__()
    jobs.sort(key=lambda x: (x[0], x[1]))
    while jobs:
        if start.__le__(jobs[0][0]): #실행 중인 작업이 없을 때
            time, processing = jobs.pop(0)
            start = (time + processing)
            answer += processing
        else:
            heap = get_heapq(start, jobs)
            time, processing = heapq.heappop(heap)[::-1]
            jobs.remove([time, processing])
            wait = start - time
            answer += (wait + processing)
            start += processing
    return answer // len_job


print(get_heapq(5,[[0,5],[3,8],[7,8]]))
