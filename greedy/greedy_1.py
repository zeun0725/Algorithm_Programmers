# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    # 여분을 가지고 있는 아이가 잃어버릴 수 있음 -> 이 부분 전처리
    num_res = [x for x in reserve if x not in lost]
    num_lost = [x for x in lost if x not in reserve]
    for i in num_res:
        if i-1 in num_lost:
            num_lost.remove(i-1)
        elif i+1 in num_lost:
                num_lost.remove(i+1)
    return n-len(num_lost)