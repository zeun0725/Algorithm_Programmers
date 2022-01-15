from collections import defaultdict, Counter
from functools import reduce


def solution(id_list, report, k):
    answer = defaultdict(int)
    for id in id_list:
        answer[id] = 0
    black_list = []
    report_list = defaultdict(list)
    for _report in set(report):
        user1, user2 = _report.split(' ')
        report_list[user1].append(user2)

    cnt_report = Counter(reduce(lambda x,y: x+y, report_list.values()))
    for user, report in cnt_report.items():
        if report >= k:
            black_list.append(user)
    for user, rep_user in report_list.items():
        answer[user] = len(set(rep_user).intersection(set(black_list)))
    return list(answer.values())


solution(["muzi", "frodo", "apeach", "neo"],
         ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
         2)