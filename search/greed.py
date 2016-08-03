__author__ = 'uiandwe'
#http://blog.eairship.kr/266
if __name__ == '__main__':
    coin = [10, 5, 1] #동전 종류
    count = [0, 0, 0]

    m = 19 #원하는 값
    i = 0
    f = 0

    while i < len(coin):
        if coin[i] > m:
            i += 1
        elif coin[i] < m:
            m -= coin[i]
            count[i] += 1
        else:
            f = 1
            count[i] += 1
            break

    print(count)



