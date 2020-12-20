# 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686

import re


def solution(files):
    answer = dict()
    for file in files:
        head = re.findall('[ a-zA-Z.-]+', file)[0]
        number = re.findall('[0-9]+', file)[0][:5]
        answer[file] = [head.lower(), int(number)]

    return [ans[0] for ans in sorted(answer.items(), key=lambda x:(x[1][0], x[1][1]))]