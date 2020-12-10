# 방금 그 곡
# https://programmers.co.kr/learn/courses/30/lessons/17683


def get_ing_time(time1, time2):
    start_time = time1.split(':')
    end_time = time2.split(':')
    return (int(end_time[0]) - int(start_time[0])) * 60 + (int(end_time[1]) - int(start_time[1]))


def solution(m, musicinfos):
    answer = ''
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        len_music = len(info[3])
        idx = 0
        ing_time = get_ing_time(info[0], info[1]) #재생시간
        while ing_time > 0:
            pass
            #구현 해야 함

    return answer