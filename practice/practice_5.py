from collections import Counter


def solution(s):
    s_count = Counter(s.lower())
    return True if s_count['p'] == s_count['y'] else False