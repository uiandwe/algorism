__author__ = 'uiandwe'

def e028():
    a, s, k = 1, 1, 2

    for _ in range(1, 501):
        for _ in range(4):
            a += k
            s += a
        k += 2

    print(s)

e028()