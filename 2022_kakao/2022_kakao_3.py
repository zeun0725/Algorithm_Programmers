from collections import defaultdict
from datetime import datetime, time
import time
import math


def get_in_minute(s_time, e_time):
    s_time = time.mktime(datetime.strptime(s_time, '%H:%M').timetuple())
    e_time = time.mktime(datetime.strptime(e_time, '%H:%M').timetuple())
    return int(e_time - s_time) // 60


def solution(fees, records):
    car_in_queue = defaultdict(str)
    car_queue = []
    answer = []
    car_in_time = defaultdict(int)
    for record in records:
        time, num, flag = record.split(' ')
        if flag == 'IN':
            car_in_queue[num] = time
            car_queue.append(num)
        else:
            in_time = get_in_minute(car_in_queue[num], time)
            car_queue.remove(num)
            car_in_time[num] += in_time
    for car in car_queue:
        in_time = get_in_minute(car_in_queue[car], "23:59")
        car_in_time[car] += in_time
    for car, times in sorted(car_in_time.items(), key=lambda x: x[0]):
        if times >= fees[0]:
            answer.append(fees[1] + (math.ceil((times - fees[0]) / fees[2]) * fees[3]))
        else:
            answer.append(fees[1])
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
                "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))


print(math.ceil(3/5))