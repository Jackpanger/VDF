from PrimeUtils import *
import time
from math import gcd
# 类群
class ClassGroup:
    def __init__(self, discriminant):
        self.discriminant = discriminant

    def identity(self):
        return (1, 0, (1 - self.discriminant) // 4)

    def reduce(self, a, b, c):
        while a > c or (a == c and b < 0):
            s = (c + b) // (c + c)
            a, b, c = c, -b + 2 * s * c, c * s * s - b * s + a
        return (a, b, c)

    def compose(self, a1, b1, c1, a2, b2, c2):
        g = gcd(a1, gcd(a2, (b1 + b2) // 2))
        a3 = a1 * a2 // g ** 2
        b3 = (b2 + b1) % (2 * a3)
        c3 = (b3 * b3 - self.discriminant) // (4 * a3)
        return self.reduce(a3, b3, c3)

    def square(self, a, b, c):
        return self.compose(a, b, c, a, b, c)

    def power(self, a, b, c, k):
        result = self.identity()
        while k > 0:
            if k % 2 == 1:
                result = self.compose(*result, a, b, c)
            a, b, c = self.square(a, b, c)
            k //= 2
        return result

    def normalize(self, a, b, c):
        if -a < b <= a:
            return (a, b, c)
        r = (a - b) // (2 * a)
        b, c = b + 2 * r * a, a * r * r + b * r + c
        return (a, b, c)

    # def serialize(self, a, b, c):
    #     a, b, c = self.reduce(a, b, c)
    #     int_size = (self.discriminant.bit_length() + 16) >> 4
    #     return b''.join(x.to_bytes(int_size, 'big', signed=True) for x in (a, b))

    # @classmethod
    # def from_bytes(cls, data, discriminant):
    #     int_size = (discriminant.bit_length() + 16) >> 4
    #     a = int.from_bytes(data[:int_size], 'big', signed=True)
    #     b = int.from_bytes(data[int_size:], 'big', signed=True)
    #     c = (b * b - discriminant) // (4 * a)
    #     return (a, b, c)


# VDF评估
def vdf_eval(discriminant, a, b, c, iterations):
    group = ClassGroup(discriminant)
    return group.power(a, b, c, 1 << iterations)


# VDF证明
def vdf_prove(discriminant, a, b, c, iterations, l):
    group = ClassGroup(discriminant)
    q = 1 << (iterations - l)
    r = 1 << l
    a, b, c = group.power(a, b, c, q)
    pi = group.power(a, b, c, r // l)
    return  pi


# VDF验证
def vdf_verify(discriminant, a, b, c, iterations, proof, l):
    group = ClassGroup(discriminant)
    a, b, c = group.normalize(a, b, c)
    y = group.power(a, b, c, 1 << iterations)
    pi = proof
    r = 1 << iterations % l
    left = group.compose(*group.power(*pi, l), *group.power(a, b, c, r))
    right = group.normalize(*y)
    return left == right


# 测试
if __name__ == "__main__":
    discriminant = -131653324254138636653163861414331698305531090221496467927360326686715180966094250598321899621249972220387687148397451395672779897144571112116763666653213748473909547482437246405018707472153290116227072825447643324530509016778432769802300913461285128339119844239772697652504835780459732685000796733645621728639
    iterations = 3355
    l = 1024

    a, b = 2, 1
    c = (b * b - discriminant) // (4 * a)
    t1 = time.time()
    y = vdf_eval(discriminant, a, b, c, iterations)
    t2 = time.time()
    print(f"VDF evaluation time: {t2 - t1} seconds")

    proof = vdf_prove(discriminant, a, b, c, iterations, l)

    t1 = time.time()
    assert vdf_verify(discriminant, a, b, c, iterations, proof, l)
    t2 = time.time()
    print(f"VDF verification time: {t2 - t1} seconds")
