from _collections import defaultdict

def is_true_path(visited, keys, order):
    key_list = []
    for key in keys:
        flag = False
        for idx, (x, y) in enumerate(order):
            if key.__eq__(y):
                flag = True
                if visited[x] == 1:
                    order[idx] = [-1, -1]
                    key_list.append(key)
            if key.__eq__(x):
                flag = True
                order[idx] = [-1, -1]
                key_list.append(key)
        if not flag:
            key_list.append(key)
    return key_list


def solution(n, path, order):
    answer = True
    n_node = defaultdict(list)
    path_list = []
    for x,y in path:
        n_node[x].append(y)
        n_node[y].append(x)
    keys = n_node[0]
    visited = [0]*n
    path_list.append(0)
    visited[0] = 1
    flag = False
    #keys: 갈 수 있는 모든 노드
    #temp_path: keys 중 오더까지 지켜진 노드
    for i in range(n):
        if 0 not in visited:
            flag = True
            break
        if keys == []:
            keys = n_node[0]
        while keys:
            if 0 not in visited:
                flag = True
                break
            temp = is_true_path(visited, keys, order)
            print(keys, temp,order)
            path_list += temp
            temp_keys = []
            for t in temp:
                visited[t] = 1
                temp_keys += [n for n in n_node[t] if visited[n]==0]
            keys = temp_keys
    print(flag,visited)


    return answer

solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])
# true
#solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])
#false