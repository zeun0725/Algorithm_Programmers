# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

import math


def get_cases(number, divisior):
    cases = []
    while divisior < int(math.sqrt(number) + 1):
        if number % divisior == 0:
            cases.append([number // divisior, divisior])
        divisior += 1
    return cases


def solution(brown, yellow):
    carpet = brown + yellow
    answer = get_cases(carpet, 3)
    yellow_answer = get_cases(yellow, 1)
    for carpet in answer:
        for yellow in yellow_answer:
            if yellow[0] + 2 <= carpet[0] and yellow[1] + 2 <= carpet[1]:
                return carpet