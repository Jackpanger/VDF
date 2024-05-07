from PrimeUtils import *


class VDF:
    t = None

    def __init__(self, group):
        self.l = None
        self.group = group

    # VDF评估
    def vdf_eval(self):
        if self.t is None:
            self.t = pow(2, self.group.T)
        return self.group.power(self.t)

    def vdf_prove(self, l):
        if self.l is None:
            self.l = l
        return self.group.power(self.t // l)

    # VDF验证
    def vdf_verify(self, pi, y):
        return self.group.compose(self.group.power_with_base(pi, self.l), self.group.power(self.t % self.l)) == y
