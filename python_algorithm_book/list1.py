# 두 수의 합
from typing import List

# 베스트 방법은 아님, 근데 브루쓰-포쓰 보다 낫다
# def solution(nums: List[int], target: int) -> List[int]:
#     for idx, num in enumerate(nums):
#         complement = target - num
#         if complement in nums[idx + 1:]:
#             return nums.index(num), nums[idx + 1:].index(complement) + (idx + 1)


# 베스트 방법
def solution(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for idx, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], idx]
        nums_map[num] = idx

print(solution([1,2,3,4,5,6,7], 9))
