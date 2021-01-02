from itertools import permutations
import re


def get_value(idx, oper, nums):
    if oper == '+':
        return int(nums[idx]) + int(nums[idx + 1])
    if oper == '-':
        return int(nums[idx]) - int(nums[idx + 1])
    if oper == '*':
        return int(nums[idx]) * int(nums[idx + 1])


def solution(expression):
    answer = 0
    origin_operator = [exp for exp in expression if exp in ('+', '-', '*')]
    operator_list = list(permutations(set(origin_operator), set(origin_operator).__len__()))
    origin_num_list = re.split('[+,\-,*]', expression)

    while operator_list:
        operator = origin_operator.copy()
        num_list = origin_num_list.copy()
        for oper in operator_list[0]:
            while oper in operator:
                idx = operator.index(oper)
                num_list = num_list[:idx] + [get_value(idx, oper, num_list)] + num_list[idx + 2:]
                operator.pop(idx)
        answer = max(answer, abs(int(num_list[0])))
        operator_list = operator_list[1:]
    return answer

print(solution("50*6-3*2"))