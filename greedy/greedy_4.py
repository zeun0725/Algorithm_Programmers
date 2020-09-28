# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort(reverse=True)
    index = 0 # 앞에서부터 탐색
    reindex = len(people) - 1 # 뒤에서부터 탐색
    while index <= reindex:
        if people[index] + people[reindex] <= limit:
            reindex -= 1
        index += 1
    return index