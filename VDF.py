from PrimeUtils import *


class VDF:
    t = None

    def __init__(self, group):
        self.l = None
        self.group = group

    def random_l(self, bits):
        self.l = generate_prime(bits)
        return self.l

    # VDF评估
    def vdf_eval(self):
        if self.t is None:
            self.t = self.group.power_with_base(2, self.group.T)
        return self.group.power(self.t)

    def vdf_prove(self, l):
        return self.group.power(self.t // l)

    # VDF验证
    def vdf_verify(self, pi, y):
        return self.group.power_with_base(pi, self.l) * self.group.power(self.t % self.l) == y
