__author__ = 'root'


if __name__ == '__main__':
    cn = 4
    coin = [1, 2, 5, 10]

    money = 20

    d = []
    for i in range(21):
        d.append(0)
    d[0] = 1

    for i in reversed(range(cn)):
        for j in range(coin[i], money+1):
            d[j] += d[j-coin[i]]

    print(d[money])