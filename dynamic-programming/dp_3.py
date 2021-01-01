def init_setting(m, n, s_map, puddles):
    s_map[0] = [1] * (s_map[0].__len__())
    for idx, section in enumerate(s_map):
        s_map[idx][0] = 1
    if puddles[0]:
        for x, y in puddles:
            s_map[y - 1][x - 1] = -1
    for _n in range(n):
        for _m in range(m):
            if s_map[_n][_m].__eq__(-1):
                if _n.__eq__(0) and _m.__ne__(m - 1):
                    s_map[_n][_m + 1] = -1
                if _m.__eq__(0) and _n.__ne__(n - 1):
                    s_map[_n + 1][_m] = -1


def get_shortest_path(m, n, s_map):
    for idx in range(1, n):
        for idx2 in range(1, m):
            if s_map[idx][idx2].__eq__(-1):
                continue
            elif s_map[idx - 1][idx2].__eq__(-1) or s_map[idx][idx2 - 1].__eq__(-1):
                s_map[idx][idx2] = max(s_map[idx - 1][idx2], s_map[idx][idx2 - 1])
            else:
                s_map[idx][idx2] = s_map[idx - 1][idx2] + s_map[idx][idx2 - 1]


def solution(m, n, puddles):
    school_map = [[0] * m for _ in range(n)]
    init_setting(m, n, school_map, puddles)
    get_shortest_path(m, n, school_map)
    return school_map[-1][-1] % 1000000007 if school_map[-1][-1].__gt__(0) else 0
