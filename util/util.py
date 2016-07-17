__author__ = 'uiandwe'


class util():

    def multiply1536(self, x, y):
        if x.bit_length() <= 1536 or y.bit_length() <= 1536:  # Base case
            return x * y

        else:
            n = max(x.bit_length(), y.bit_length())
            half = (n + 32) // 64 * 32
            mask = (1 << half) - 1
            xlow = x & mask
            ylow = y & mask
            xhigh = x >> half
            yhigh = y >> half

            a = self.multiply(xhigh, yhigh)
            b = self.multiply(xlow + xhigh, ylow + yhigh)
            c = self.multiply(xlow, ylow)
            d = b - a - c
            return (((a << half) + d) << half) + c

    def Karatsuba(self, number1, number2, N):

        if N == 1:
            return number1*number2

        if N % 2 == 1:
            N += 1

        exp = N//2
        pw = pow(10, exp)

        num1, num2 = number1 // pw, number1 % pw
        num3, num4 = number2 // pw, number2 % pw

        U = self.Karatsuba(num1, num3, exp)
        V = self.Karatsuba(num2, num4, exp)

        N1 = num1-num2
        N2 = num3-num4


        W = self.Karatsuba(N1, N2, exp)
        Z = U+V-W

        result = pow(10, N) * U + pow(10, N/2) * Z + V

        return result




if __name__ == '__main__':
    u = util()
    print(999*99)
    num = u.Karatsuba(999, 99, 3)
    print(num)