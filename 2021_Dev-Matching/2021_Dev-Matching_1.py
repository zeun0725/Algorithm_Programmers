# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

RANK = 7

def solution(lottos, win_nums):
    answer = []
    min_rslt = len(set(lottos).intersection(set(win_nums)))
    max_rslt = min_rslt + lottos.count(0)
    answer.append(RANK - min_rslt if RANK - min_rslt < 7 else 6)
    answer.append(RANK - max_rslt if RANK - max_rslt < 7 else 6)
    answer.sort()
    return answer