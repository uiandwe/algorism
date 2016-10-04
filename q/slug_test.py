__author__ = 'uiandwe'
import math

def quick(array_list):
    if len(array_list) <= 1:
        return array_list

    pivot = array_list[int(len(array_list)/2)]
    less = []
    more = []
    equal = []
    for val in array_list:
        if pivot < val:
            more.append(val)
        elif pivot == val:
            equal.append(val)
        else:
            less.append(val)
    return quick(less)+quick(equal)+quick(more)


def binary(array_list, search_value):
    print("find value : ", search_value)
    if array_list[0] > search_value:
        return array_list[0]
    if array_list[-1] < search_value:
        return array_list[-1]

    piovt = math.ceil(len(array_list)/2)
    distance = array_list[-1]
    close_value = 0

    for index in range(2, len(array_list)):
        next_piovt = len(array_list)/pow(2, index)

        if next_piovt <= 0:
            next_piovt = 1
        else:
            next_piovt = math.ceil(next_piovt)

        if abs(array_list[piovt]-search_value) < distance:
            distance = abs(array_list[piovt]-search_value)
            close_value = array_list[piovt]
        elif array_list[piovt] > search_value:
            piovt -= next_piovt
        else:
            piovt += next_piovt

    return distance, close_value

if __name__ == '__main__':

    import random

    temp_list = [random.randint(1, 1000) for i in range(1, 20)]

    temp_list = quick(temp_list)
    print(temp_list)
    print(binary(temp_list, random.randint(1, 1000)))