from collections import defaultdict

def calc_per_val(value):
    return value // 10

def get_next_rl(user, value, rl_dict, result):
    per_value = calc_per_val(value)
    result[user] += value - per_value
    return rl_dict[user], per_value

def solution(enroll, referral, seller, amount):
    rl_dict = dict()
    result = defaultdict(int)
    answer = []
    center = 'minho'
    for enrl, rfrl in zip(enroll, referral):
        if rfrl == '-':
            rl_dict[enrl] = center
        else:
            rl_dict[enrl] = rfrl
        result[enrl] = 0
    for user, value in zip(seller, amount):
        value *= 100
        while value > 0 and user != 'minho':
            user, value = get_next_rl(user, value, rl_dict, result)
    return list(result.values())


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])