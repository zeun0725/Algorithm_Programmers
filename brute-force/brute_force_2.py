# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839#


import itertools
import math

def solution(numbers):
    answer = 0
    nums = [num for num in numbers]
    prime_num=[] # 소수 담을 리스트

    for idx in range(1,len(nums)+1):
        #가능한 모든 순열 저장
        prime_num += set(map(int, map(''.join, itertools.permutations(nums, idx))))

    # 짝수 거르는 작업
    prime_num = {num for num in prime_num if (num % 2 == 1 and num > 1) or num == 2}
    for num in prime_num:
        if num == 2 or num == 3 or num == 5:
            answer += 1
            continue
        divide=3
        for _ in range(3, int(math.sqrt(num))+1):
            if num % divide != 0:
                divide += 1
            else:
                break

        if divide == int(math.sqrt(num))+1: # 소수일때
            answer += 1
    return answer