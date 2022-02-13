import re

def solution(pattern: str) -> bool:
    re_pattern = re.sub('[^a-z0-9]', '', pattern.lower())
    return re_pattern == re_pattern[::-1]


print(solution('race a car'))

