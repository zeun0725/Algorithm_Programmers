# 방금 그 곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

def get_ing_time(time1, time2):
    start_time = list(map(int, time1.split(':')))
    end_time = list(map(int, time2.split(':')))
    return (end_time[0] - start_time[0]) * 60 + (end_time[1] - start_time[1])

def hash_to_lower(musics):
    while musics.find('#') != -1:
        h_idx = musics.find('#')
        musics = musics[:h_idx-1] + musics[h_idx-1].lower() + musics[h_idx+1:]
    return musics

def solution(m, musicinfos):
    answer = []
    m = hash_to_lower(m)
    len_m = len(m)
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        lyrics = hash_to_lower(info[3])
        len_lyric = len(lyrics)
        ing_time = get_ing_time(info[0], info[1])
        ing_time_2 = ing_time
        music = lyrics*(ing_time//len_lyric)
        music += lyrics[:ing_time-len(music)]
        if m in music:
            answer.append([ing_time_2, info[2]])
    if not answer:
        return "(None)"
    answer.sort(key=lambda x: -x[0])
    return answer[0][1]


# test case 12번 통과 못한 소스코드
# https://programmers.co.kr/questions/6647
# 악보 1439 이하라 1439 까지 늘리고 앞에서부터 같은 음 있으면 통과 없으면 다시 처음 인덱스로..
# def get_ing_time(time1, time2):
#     start_time = list(map(int, time1.split(':')))
#     end_time = list(map(int, time2.split(':')))
#     return (end_time[0] - start_time[0]) * 60 + (end_time[1] - start_time[1])
#
# def hash_to_lower(musics):
#     while musics.find('#') != -1:
#         h_idx = musics.find('#')
#         musics = musics[:h_idx-1] + musics[h_idx-1].lower() + musics[h_idx+1:]
#     return musics
#
# def solution(m, musicinfos):
#     answer = []
#     m = hash_to_lower(m)
#     len_m = len(m)
#     for musicinfo in musicinfos:
#         info = musicinfo.split(',')
#         lyrics = hash_to_lower(info[3])
#         len_lyric = len(lyrics)
#         idx = 0
#         m_idx = 0
#         music = lyrics*(1439//len_lyric)
#         music += lyrics[:1439-len(music)]
#         ing_time = get_ing_time(info[0], info[1])
#         ing_time_2 = ing_time
#         while ing_time > 0:
#             ing_time -= 1
#             if music[idx] == m[m_idx % len_m]:
#                 m_idx += 1
#                 idx += 1
#             else:
#                 m_idx = 0
#                 idx += 1
#                 continue
#
#             if (m_idx % len_m) == 0:
#                 answer.append([ing_time_2, info[2]])
#                 break
#     if not answer:
#         return "(None)"
#     answer.sort(key=lambda x: -x[0])
#     return answer[0][1]
