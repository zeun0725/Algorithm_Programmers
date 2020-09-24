# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import Counter

def solution(numbers, target):
    # +, -
    num_of_cases = 2 ** len(numbers)
    cases = []
    idx = 0
    while idx < len(numbers):
        if not cases:
            cases.append(numbers[idx])
            cases.append(-numbers[idx])
        else:
            for case in cases[:]:
                cases.append(case+numbers[idx])
                cases.append(case-numbers[idx])
            cases = cases[2**idx:]
        idx += 1
    return Counter(cases[-num_of_cases:])[target]