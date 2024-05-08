from math import gcd


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def linear_congruence(a, b, m):
    g, d, e = xgcd(a, m)
    q = b // g
    r = b % g
    if r != 0:
        raise Exception
    else:
        return q * d % m, m // g


# 类群
class ClassGroup:
    def __init__(self, a, b, c, discriminant, T, l):
        self.l = l
        self.T = T
        self.Q1 = a, b, c
        self.discriminant = discriminant

    def identity(self):
        return 1, self.discriminant % 4, (1 - self.discriminant) // 4

    def reduce(self, Q):
        a, b, c = self.normalize(Q)
        while a > c or (a == c and b <= 0):
            s = (c + b) // (c + c)
            a, b, c = c, -b + 2 * s * c, c * s * s - b * s + a
        return a, b, c

    def compose(self, Q1, Q2):
        a1, b1, c1 = Q1
        a2, b2, _ = Q2
        g = (b1 + b2) // 2
        h = (b1 - b2) // 2
        w = gcd(a1, a2, g)
        j, s, t, u = w, a1 // w, a2 // w, g // w
        mu, v = linear_congruence(t * u, h * u + s * c1, s * t)
        lamda, sigma = linear_congruence(t * v, h - t * mu, s)
        k = mu + v * lamda
        l, m = (k * t - h) // s, (t * u * k - h * u - c1 * s) // s * t
        return s * t, j * u - (k * t + l * s), k * l - j * m

    def square(self, Q):
        return self.compose(Q, Q)

    def power(self, iteration):
        return self.power_with_base(self.Q1, iteration)

    def power_with_base(self, base, iteration):
        a, b, c = base
        result = self.identity()
        if iteration == 1:
            return self.compose(self.Q1, result)
        while iteration > 0:
            if iteration % 2 == 1:
                result = self.compose(result, (a, b, c))
            a, b, c = self.square(result)
            iteration //= 2
        return result

    def normalize(self, Q):
        a, b, c = Q
        if -a < b <= a:
            return a, b, c
        r = (a - b) // (2 * a)
        return a, b + 2 * r * a, a * r * r + b * r + c

    def random_l(self):
        return self.l

