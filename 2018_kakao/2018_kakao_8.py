from datetime import datetime, timedelta

def get_time_section(s_time, e_time, log_list):
    ans = 0
    for s_log, e_log in log_list:
        if (s_log <= s_time <= e_log) or (s_time <= s_log and e_time >= e_log)  or (s_log <= e_time <= e_log):
            ans += 1
            continue
    return ans

def get_datetime_format(logs):
    e_time = datetime.strptime(logs[0], "%Y-%m-%d %H:%M:%S.%f")
    s_time = e_time - timedelta(milliseconds=float(logs[1]) * 1000 - 1)

    return [s_time, e_time]

def get_log_data(logs):
    log_list = []
    for log in logs:
        log_form = [log[0] + ' ' + log[1], log[2][:-1]]
        log_list.append(get_datetime_format(log_form))
    log_list.sort(key=lambda x: (x[0], x[1]))
    return log_list

def get_max_section(log_list):
    answer = 0
    for log in log_list:
        for m_time in range(3):
            start_time = log[0] + timedelta(seconds=m_time)
            end_time = start_time + timedelta(seconds=0.999)
            if start_time > log[1]:
                start_time = log[1]
                end_time = log[1] + timedelta(seconds=0.999)
            answer = max(answer, get_time_section(start_time, end_time, log_list))
    return answer

def solution(lines):
    logs = [line.split(' ') for line in lines]
    log_list = get_log_data(logs)
    return get_max_section(log_list)