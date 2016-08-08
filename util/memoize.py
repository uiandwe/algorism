__author__ = 'uiandwe'


def memoize(func):
    tempMemo = dict()
    def wrapped(n):
        if n in tempMemo:
            return tempMemo[n]
        result = func(n)
        tempMemo[n] = result
        return result
    return wrapped


@memoize
def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)



if __name__ == '__main__':
    import time

    #processing start
    start_time = time.time()
    print(fib(35))
    #processing end
    end_time = time.time()


    #print processing time
    print(end_time - start_time)
