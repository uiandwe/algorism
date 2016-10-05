__author__ = 'uiandwe'

i_max = 100000

map = []
visit = []
dist = []
start = 0
end = 7
node = 7


def input():
    for i in range(node):
        temp_array = []
        for j in range(node):
            temp_array.append(i_max)
        map.append(temp_array)

    map[0][1] = 4
    map[0][2] = 2
    map[1][3] = 1
    map[1][4] = 2
    map[2][3] = 7
    map[2][5] = 3
    map[3][6] = 3
    map[4][6] = 1
    map[5][6] = 5

    for i in range(node):          # dist와 visit 배열 초기화
        dist.append(i_max)
        visit.append(0)


def dijkstra():

        visit_node = 0

        dist[start] = 0        # 시작점의 거리 셋팅

        for i in range(node):
            dist_min = i_max

            for j in range(node):

                if visit[j] == 0 and dist_min > dist[j]:    #갈수 있는 정점중에 가장 가까운 정점 선택
                    dist_min = dist[j]
                    visit_node = j

            for k in range(node):
                if dist[k] > dist[visit_node] + map[visit_node][k]:
                    dist[k] = dist[visit_node] + map[visit_node][k]   #방문한 정점을 통해 다른 정점까지의 거리가 짧아지는지 계산하여 누적된값 저장

            visit[visit_node] = 1   # 가장 가까운 정점으로 방문, i정점에서 가장 가까운 최단경로 visit_node


if __name__ == '__main__':
    input()
    dijkstra()
    print(dist)