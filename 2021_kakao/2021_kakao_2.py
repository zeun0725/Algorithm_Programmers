# 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
from collections import Counter
from itertools import combinations


def solution(orders, course):
    order_list = []
    for idx, _c in enumerate(course):
        order_list.append([])
        for order in orders:
            order_list[idx] += list(combinations(order, _c))
    answer = []

    for order in order_list:
        _order = [''.join(sorted(oo)) for oo in order]
        cnt_order = Counter(_order)
        if not cnt_order:
            continue
        max_cnt = max(cnt_order.values())
        if max_cnt < 2:
            continue
        for od, cnt in cnt_order.items():
            if cnt == max_cnt:
                answer.append(od)
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))