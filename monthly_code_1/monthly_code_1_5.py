# 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    rm_cnt = 0
    rm_idx = 0
    while s != "1":
        s1 = s.replace("0", "")
        rm_cnt += len(s) - len(s1)
        s = bin(len(s1))[2:]
        rm_idx += 1

    return [rm_idx, rm_cnt]
