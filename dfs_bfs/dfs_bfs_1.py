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

#=========================================


def get_value(numbers, value, target):
    if not numbers:
        if value.__eq__(target):
            return 1
        return 0
    return get_value(numbers[1:], value + numbers[0], target) + get_value(numbers[1:], value - numbers[0], target)

def solution(numbers, target):
    return get_value(numbers[1:], numbers[0], target) + get_value(numbers[1:], -numbers[0], target)
