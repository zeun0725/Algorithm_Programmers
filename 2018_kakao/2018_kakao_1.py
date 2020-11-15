# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

def get_two_string(text):
    return [text[idx] + text[idx + 1] for idx, char in enumerate(text[:-1]) if
            'a' <= text[idx] <= 'z' and 'a' <= text[idx + 1] <= 'z']


def get_jaccard_similarity(str1, str2):
    similar = 0
    for char in str1:
        if char in str2:
            similar += 1
            str2.remove(char)
    return similar / (len(str1) + len(str2))


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    two_str1 = get_two_string(str1)
    two_str2 = get_two_string(str2)
    if not two_str1 and not two_str2:
        return 65536
    return int(get_jaccard_similarity(two_str1, two_str2) * 65536)
