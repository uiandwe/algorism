__author__ = 'uiandwe'
import math


def findNearNumber(array_list, search_value):
    print("find value : ", search_value)
    if array_list[0] > search_value:
        return array_list[0]
    if array_list[-1] < search_value:
        return array_list[-1]

    piovt = math.ceil(len(array_list)/2)                        #전체 배열의 1/2지점부터 시작
    distance = array_list[-1]                                   # 가장 큰 수로 셋팅
    close_value = 0                                             # 거리 초기화

    for index in range(2, len(array_list)):

        if abs(array_list[piovt]-search_value) < distance:      #현재 값과의 거리가 더 작으면
            distance = abs(array_list[piovt]-search_value)      #거리값 재조정
            close_value = array_list[piovt]                     #가까운 값 저장
        elif abs(array_list[piovt]-search_value) == distance:
            break

        next_piovt = len(array_list)/pow(2, index)              #다음 탐색 거리 계산 (logn)

        if next_piovt <= 0:
            next_piovt = 1
        else:
            next_piovt = math.ceil(next_piovt)

        if array_list[piovt] > search_value:                   #값이 더 작았다면 - 이동
            piovt -= next_piovt
        else:
            piovt += next_piovt                                #값이 더 크다면 + 이동

    return distance, close_value

if __name__ == '__main__':

    import random

    temp_list = [random.randint(1, 1000) for i in range(1, 20)]

    temp_list = sorted(temp_list)
    find_value = random.randint(1, 1000)
    print(temp_list)
    print([abs(i-find_value) for i in temp_list])
    print(findNearNumber(temp_list, find_value))