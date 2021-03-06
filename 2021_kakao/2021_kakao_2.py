# 각 손님 단품메뉴 두개이상 주문 , 최소 2명이상ㅇ로부터 주문ㄴ된 메뉴를 코스로 만듦

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