__author__ = 'uiandwe'

'''
x만큼 간격이 있는 n개의 숫자

number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]
'''


def number_generator(x, n):
    return [i for i in range(x, x*n+x, x)]

