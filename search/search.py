__author__ = 'uiandwe'
from sorting import sorting
import math

class search():

    def binary(self, array_list, search_value):
        piovt = len(array_list)/2
        for index in range(2, len(array_list)):
            next_piovt = len(array_list)/pow(2, index)
            if next_piovt <= 0:
                next_piovt = 1

            if array_list[piovt] == search_value:
                return piovt
            elif array_list[piovt] > search_value:
                piovt -= next_piovt
            else:
                piovt += next_piovt







if __name__ == '__main__':
    s = sorting.sorting()
    search = search()
    temp_list = list(range(1, 10))
    print(temp_list)
    print(search.binary(temp_list, 8))