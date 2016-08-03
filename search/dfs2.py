__author__ = 'uiandwe'


#http://blog.eairship.kr/268

visit = [0, 0, 0, 0, 0]
map_array = [[1, 1, 1, 1, 1],
             [0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1],
             [1, 0, 1, 0, 0],
             [1, 1, 1, 1, 1]
             ]
n = len(visit)
min_search = 25



def dfs_search(x, y, l):
    if x == n-1 and y == n-1:
        if min_search > l:
            print(l)
        return

    map_array[y][x] = 0
    if y > 0 and map_array[y-1][x] != 0:
        dfs_search(x, y-1, l+1)
    if y < n-1 and map_array[y+1][x] != 0:
        dfs_search(x, y+1, l+1)
    if x > 0 and map_array[y][x-1] != 0:
        dfs_search(x-1, y, l+1)
    if x < n-1 and map_array[y][x+1] != 0:
        dfs_search(x+1, y, l+1)

    map_array[y][x] = 1


if __name__ == '__main__':

    dfs_search(0, 0, 1)
