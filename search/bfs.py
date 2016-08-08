__author__ = 'uiandwe'
import queue as queue

visit = [0, 0, 0, 0, 0, 0]
map_array = [[0, 1, 1, 0, 0, 0],
             [1, 0, 0, 1, 1, 0],
             [1, 0, 0, 1, 0, 1],
             [0, 1, 1, 0, 1, 1],
             [0, 1, 0, 1, 0, 1],
             [0, 0, 1, 1, 1, -1],
             ]
n = len(visit)
q = queue.Queue()


def bfs(v):
    visit[v] = 1
    print("start "+v)
    q.put(v)


if __name__ == '__main__':
    q = queue.Queue()
    q.put("1")
    q.put("2")
    print(q.get())
    print(q.get())
    print("!")
