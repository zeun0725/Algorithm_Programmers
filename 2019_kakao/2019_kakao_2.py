# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

import re
from collections import Counter

def solution(s):
    return [int(s[0]) for s in sorted(Counter(re.findall('\d+', s)).items(), key=lambda x: x[1], reverse=True)]
