# 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(list(answer))

print(solution([2,1,3,4,1]))