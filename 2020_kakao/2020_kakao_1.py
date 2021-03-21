# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

# 코드 간단하게 고쳐보기
def solution(s):
    answer = len(s)
    if answer == 1:
        return 1
    count = answer // 2
    while count > 0:
        copy_s = s[:]
        min_zip = 0
        pre = 1
        while len(copy_s) >= count * 2:
            if copy_s[:count] == copy_s[count:count * 2]:
                pre += 1
            elif pre != 1:
                min_zip += len(str(pre)) + count
                pre = 1
            else:
                min_zip += count
            copy_s = copy_s[count:]
        if pre == 1:
            min_zip += len(copy_s)
        else:
            min_zip += len(str(pre)) + len(copy_s)

        if min_zip < answer:
            answer = min_zip
        count -= 1
    return answer


def get_zip_num(s, num):
    s_list = [s[i:i + num] for i in range(0, len(s), num)]
    init_cnt = 1
    new_s = ''
    for idx, s in enumerate(s_list[:-1]):
        if s_list[idx] == s_list[idx + 1]:
            init_cnt += 1
            continue
        if init_cnt > 1:
            new_s += str(init_cnt)
        new_s += s_list[idx]
        init_cnt = 1
    if init_cnt > 1:
        new_s += str(init_cnt)
    new_s += s_list[idx + 1]
    return new_s


def solution(s):
    answer = len(s)
    for zip_num in range(1, len(s) // 2 + 1):
        new_s = get_zip_num(s, zip_num)
        if len(new_s) < answer:
            answer = len(new_s)
    return answer

