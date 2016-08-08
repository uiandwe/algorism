__author__ = 'uiandwe'

"""
2 ≤ a ≤ 5 이고 2 ≤ b ≤ 5인 두 정수 a, b로 만들 수 있는 a**b의 모든 조합을 구하면 다음과 같습니다.

    2**2=4,  2**3=8,  2**4=16,  2**5=32
    3**2=9,  3**3=27,  3**4=81,  3**5=243
    4**2=16,  4**3=64,  4**4=256,  4**5=1024
    5**2=25,  5**3=125,  5**4=625,  5**5=3125

여기서 중복된 것을 빼고 크기 순으로 나열하면 아래와 같은 15개의 숫자가 됩니다.

4,  8,  9,  16,  25,  27,  32,  64,  81,  125,  243,  256,  625,  1024,  3125

그러면, 2 ≤ a ≤ 100 이고 2 ≤ b ≤ 100인 a, b를 가지고 만들 수 있는 a**b는 중복을 제외하면 모두 몇 개입니까?
"""

def e029():
    a = set()
    for x in range(2, 6):
        for y in range(2, 6):
            a.add(x**y)

    print(len(a))

e029()