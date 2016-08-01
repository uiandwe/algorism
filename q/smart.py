__author__ = 'uiandwe'


def round(i):
    return int(i+0.5) if i > 0 else int(i-0.5)


def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num-1)


def strReverse(str):
    return ''.join(reversed(str))

