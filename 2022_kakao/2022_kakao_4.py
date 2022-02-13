# 동일 점수 시 어피치가 점수를 가져감
from itertools import permutations
def solution(n, info):
    answer = []
    max_score = -1
    # 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1
    # 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0
    init_score = map(lambda x: x+1, info)
    for idx, score in enumerate(init_score):
        n = n-score
        ryan_score = 10 - idx
        while True:
            n = n-score
            ryan_score += 10 - idx

    print(init_score)

    return answer
print(permutations([5], 10))
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))