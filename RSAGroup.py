from PrimeUtils import *


class RSAGroup:

    def __init__(self, T, bits):
        self.T = T
        self.bits = bits
        self.x, self.N = self.setup(bits)

    def power_with_base(self, base, iteration):
        return pow(base, iteration, self.N)

    def power(self, iteration):
        return pow(self.x, iteration, self.N)

    def setup(self, bits):
        p = generate_prime(bits // 2)
        q = generate_prime(bits // 2)
        while p == q:
            q = generate_prime(bits // 2)
        N = p * q
        return random.randint(0, N - 1), p * q


class RSAProver:
    t = None

    def __init__(self, x, T, N):
        self.x = x
        self.T = T
        self.N = N

    def vdf_eval(self):
        if self.t is None:
            self.t = pow(2, self.T, self.N)
        return pow(self.x, self.t, self.N)

    def vdf_prove(self, l):
        return pow(self.x, self.t // l, self.N)


class RSAVerifier:
    t, l = None, None

    def __init__(self, x, T, N):
        self.x = x
        self.T = T
        self.N = N

    def random_l(self, bits):
        self.l = generate_prime(bits)
        return self.l

    # VDF验证
    def vdf_verify(self, pi, y):
        if self.t is None:
            self.t = pow(2, self.T, self.N)
        r = self.t % self.l
        return pow(pi, self.l, self.N) * pow(self.x, r, self.N) == y
