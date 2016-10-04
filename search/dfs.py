__author__ = 'uiandwe'

#http://blog.eairship.kr/268

visit = [0, 0, 0, 0, 0, 0, 0, 0]
map_array = [[0, 1, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [0, 0, 0, 1, 1, 1, 1, -1],
             ]


def dfs_search(v):
    visit[v] = 1
    for i in range(len(map_array)):
        if map_array[v][i] == 1 and visit[i] == 0:
            print(v, i)
            dfs_search(i)


if __name__ == '__main__':
    print(len(map_array))
    dfs_search(0)