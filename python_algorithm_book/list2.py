# 빗물 트래핑
from typing import List
"""
투포인터 최대 이동 => O(n) 에 풀이 가능
최대 지점에서 좌우 포인터가 만나게 됨
"""

def trap(height: List[int]) -> int:
    if not height:
        return 0
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

"""
스택 쌓기 => O(n) 에 풀이 가능
변곡점 만날 때 마다 pop 해서 비교
"""

def trap(height: List[int]) -> int:
    stack = []
    volume = 0
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not len(stack):
                break
            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters
        stack.append(i)
    return volume

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
