# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def padding(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    for index, num in enumerate(lock):
        lock[index] = [-1] * (len_key - 1) + lock[index] + [-1] * (len_key - 1)
    for _ in range(len_key - 1):
        lock.insert(0, [-1] * (len_key * 2 - 2 + len_lock))
        lock.append([-1] * (len_key * 2 - 2 + len_lock))

def rotate(key):
    r_key = []
    for k in list(zip(*key)):
        r_key.append(list(reversed(k)))
    return r_key

def solution(key, lock):
    answer = False
    lock_cnt = 0
    for l in lock:
        lock_cnt += l.count(0)
    padding(key, lock)
    key2 = rotate(key)
    key3 = rotate(key2)
    key4 = rotate(key3)

    for i in range(len(lock) - len(key) + 1):
        for j in range(len(lock) - len(key) + 1):
            for setkey in [key, key2, key3, key4]:
                cnt = lock_cnt
                escape = True
                for key_i in range(len(key)):
                    for key_j in range(len(key)):
                        if lock[i + key_i][j + key_j] == 1 and setkey[key_i][key_j] == 1:
                            escape = False
                            break
                        if lock[i + key_i][j + key_j] == 0 and setkey[key_i][key_j] == 1:
                            cnt -= 1

                    if not escape:
                        break
                if cnt == 0 and escape:
                    return True
    return False