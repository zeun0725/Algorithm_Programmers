# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

### 효율성 시간 초과
import re

def match_info(idx, val, info_list, match_idx):
    if idx == -1:
        for i in match_idx[:]:
            if int(info_list[i][idx]) < int(val):
                match_idx.remove(i)
    else:
        for i in match_idx[:]:
            if info_list[i][idx] != val:
                match_idx.remove(i)
    return match_idx


def solution(info, query):
    info_list = []
    for _info in info:
        info_list.append(_info.split(" "))

    query_list = []
    for q in query:
        q = q.replace("and", "")
        q = re.sub(' {2,}', ' ', q)
        query_list.append(q.split(" "))

    answer = []
    for query in query_list:
        match_idx = [idx for idx in range(len(info_list))]
        for i, q in enumerate(query):
            if q == '-':
                continue
            if i == (len(query) - 1):
                i = -1
            match_idx = match_info(i, q, info_list, match_idx)
        answer.append(match_idx.__len__())
    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])