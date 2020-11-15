# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict


def get_total_plays(genres, plays):
    genre_dic = defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_dic[genre] += play
    return sorted(genre_dic.items(), key=lambda x: x[1], reverse=True)


def solution(genres, plays):
    answer = []
    sort_genre_dic = get_total_plays(genres, plays)
    genre_play = [[genre, play] for genre, play in zip(genres, plays)]

    for idx, _ in enumerate(plays):
        genre_play[idx].append(idx)
    genre_play = sorted(genre_play, key=lambda x: x[1], reverse=True)

    for genre in sort_genre_dic:
        temp_answer = [play[2] for play in genre_play if play[0] == genre[0]]
        answer += temp_answer[:2]

    return answer
