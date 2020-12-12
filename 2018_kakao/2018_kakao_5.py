# 방금 그 곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

def get_ing_time(time1, time2):
    start_time = list(map(int, time1.split(':')))
    end_time = list(map(int, time2.split(':')))
    return (end_time[0] - start_time[0]) * 60 + (end_time[1] - start_time[1])

def hash_to_lower(musics):
    if '#' not in musics:
        return musics
    re_music = ''
    for idx, music in enumerate(musics):
        if musics[idx] == '#':
            continue
        if idx < len(musics)-1 and musics[idx+1] == '#':
            re_music += music.lower()
        else:
            re_music += music
    return re_music

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
        while ing_time > 0:
            ing_time -= 1
            music = lyrics * (len_m // len_lyric)
            music += lyrics[:len_m - len(music)]
            if m in music:
                answer.append([ing_time_2, info[2]])
                break
            lyrics = lyrics[1:] + lyrics[0]
    if not answer:
        return "(None)"
    answer.sort(key=lambda x: -x[0])
    return answer[0][1]


# test case 12번 통과 못한 소스코드
#
# def get_ing_time(time1, time2):
#     start_time = time1.split(':')
#     end_time = time2.split(':')
#     return (int(end_time[0])-int(start_time[0]))*60+(int(end_time[1])-int(start_time[1]))
#
# def hash_to_lower(music):
#     music2 = ''
#     for i, m in enumerate(music):
#         if music[i] == '#':
#             continue
#         if i < len(music)-1 and music[i+1]=='#':
#             music2 += m.lower()
#         else:
#             music2 += m
#     return music2
#
# def solution(m, musicinfos):
#     answer = []
#     m = hash_to_lower(m)
#     len_m = len(m)
#     for idx, musicinfo in enumerate(musicinfos):
#         info = musicinfo.split(',')
#         info_test = hash_to_lower(info[3])
#         len_music = len(info_test)
#         idx = 0
#         m_idx = 0
#         music = info_test*(1439//len_music)
#         music += info_test[:1439-len(music)]
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
#             if (m_idx % len_m) == 0:
#                 answer.append([ing_time_2, idx, info[2]])
#                 break
#
#     if not answer:
#         return "(None)"
#     answer.sort(key=lambda x: (-x[0],x[1]))
#     return answer[0][2]
