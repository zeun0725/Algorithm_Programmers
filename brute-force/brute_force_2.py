# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839#


import itertools
import math

def get_prime_num(num):
    divide = 3
    for divisior in range(divide, int(math.sqrt(num)) + 1):
        if num % divisior == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = [num for num in numbers]
    prime_num = [] # 소수 담을 리스트

    for idx in range(1,len(nums)+1):
        #가능한 모든 순열 저장
        prime_num += set(map(int, map(''.join, itertools.permutations(nums, idx))))

    # 짝수 거르는 작업
    prime_num = {num for num in prime_num if (num % 2 == 1 and num > 1) or num == 2}
    for num in prime_num:
        if num in [2, 3, 5]:
            answer += 1
            continue
        answer += get_prime_num(num)
    return answer



#==============


from itertools import permutations
import math

def get_prime_num(num, idx):
    sqrt_num = int(math.sqrt(num))
    while sqrt_num >= idx:
        if num % idx == 0:
            return 0
        idx += 1
    return 0 if num == 1 else 1

def solution(numbers):
    nums = list(numbers)
    answer = 1 if '2' in nums else 0
    prmt_nums = set()
    for idx in range(1, len(nums)+1):
        prmt_nums.update(set(map(int, [''.join(num) for num in permutations(nums,idx)])))
    for prmt_num in prmt_nums:
        if prmt_num & 1 == 0:
            continue
        answer += get_prime_num(prmt_num, 3)
    return answer