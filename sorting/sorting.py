__author__ = 'uiandwe'


class sorting:
    #n^2
    def bubble(self, array_list):

        for i, i_val in enumerate(array_list):
            for j, j_val in enumerate(array_list):
                if array_list[i] < array_list[j]:
                    array_list[i], array_list[j] = array_list[j], array_list[i]

        return array_list

    def selection(self, array_list):
        for i, i_val in enumerate(array_list):
            select_index_val = array_list[i]
            for j, j_val in enumerate(array_list):
                if select_index_val < array_list[j]:
                    array_list[i], array_list[j] = array_list[j], array_list[i]
                    select_index_val = array_list[i]

        return array_list

    def insertion(self, array_list):

        for i, i_val in enumerate(array_list):
            for j in (1, i):
                if array_list[(j-1)] > array_list[j]:
                    array_list[i], array_list[j] = array_list[j], array_list[i]

        return array_list

    #nlogn
    def merge(self, array_list):
        if len(array_list) <= 1:
            return array_list

        m = len(array_list) // 2
        l = self.merge(array_list[:m])
        r = self.merge(array_list[m:])

        result = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        result += l[i:]
        result += r[j:]
        return result

    def quick(self, array_list):
        if len(array_list) <= 1:
            return array_list

        pivot = array_list[len(array_list)/2]
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
        return self.quick(less)+self.quick(equal)+self.quick(more)

if __name__ == '__main__':
    s = sorting()
    temp_list = [9, 2, 6, 1, 8, 10, 4, 5, 3, 7]
    print(s.bubble(temp_list))
    print(s.selection(temp_list))
    print(s.insertion(temp_list))
    print(s.merge(temp_list))
    print(s.quick(temp_list))