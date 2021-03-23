# 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum([_a * _b for _a, _b in zip(a, b)])