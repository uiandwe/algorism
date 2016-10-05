__author__ = 'uiandwe'

i_max = 100000

a = []
visit = []
dist = []
start = 0
end = 7
n = 7

def input():
    for i in range(n):
        temp_array = []
        for j in range(n):
            temp_array.append(i_max)
        a.append(temp_array)

    a[0][1] = 4
    a[0][2] = 2
    a[1][3] = 1
    a[1][4] = 2
    a[2][3] = 7
    a[2][5] = 3
    a[3][6] = 3
    a[4][6] = 1
    a[5][6] = 5


    for i in range(n):
        dist.append(i_max)
        visit.append(0)



def dijkstra():

        v = 0

        dist[start] = 0        # 시작점의 거리 셋팅

        for i in range(n):
            dist_min = i_max

            for j in range(n):

                if visit[j] == 0 and dist_min > dist[j]:    #갈수 있는 정점중에 가장 가까운 정점 선택
                    dist_min = dist[j]
                    v = j

            for k in range(n):
                if dist[k] > dist[v] + a[v][k]:
                    dist[k] = dist[v] + a[v][k] #방문한 정점을 통해 다른 정점까지의 거리가 짧아지는지 계산하여 누적된값 저장

            visit[v] = 1   # 가장 가까운 정점으로 방문, i정점에서 가장 가까운 최단경로 v


if __name__ == '__main__':
    input()
    dijkstra()
    print(dist)