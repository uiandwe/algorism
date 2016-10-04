__author__ = 'uiandwe'



"""
list comprehension이 일반 리스트 생성보다 딱 두배 빠름.
"""


if __name__ == '__main__':
    import time

    #processing start
    start_time = time.time()
    [x for x in range(1, 10000000)]
    #processing end
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()

    temp_list = []
    for x in range(1, 10000000):
        temp_list.append(x)

    end_time = time.time()
    print(end_time - start_time)


