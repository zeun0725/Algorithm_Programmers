# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3

from itertools import combinations


def is_prime_number(num): #소수인지 구하는 함수
    div = 3
    while num > div:
        if num % div == 0:
            return False
        div += 1
    return True


def solution(nums):
    answer = 0
    num_list = combinations(nums, 3)
    for num in num_list:
        key = sum(num)
        if key & 1 == 1: #홀수 일 때
            answer += is_prime_number(key)

    return answer