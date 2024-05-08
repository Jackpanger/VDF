from RSAGroup import *
from ClassGroup import *
from VDF import *
import unittest


def testVDF(VDF, group):
    y = VDF.vdf_eval()  # send y to verifier
    print("y: " + str(y))

    # generate random l to prover
    l = group.random_l()
    print("l: " + str(l))

    # generate pi
    pi = VDF.vdf_prove(l)
    print("pi: " + str(pi))

    # verifier
    return VDF.vdf_verify(pi, y)


class TestVDF(unittest.TestCase):
    def setUp(self):
        self.T = 3000

    def test_rsa_group(self):
        """group 1 """
        # RSA group
        bits = 2048
        group = RSAGroup(self.T, bits)
        vdf = VDF(group)
        self.assertTrue(testVDF(vdf, group))
        print("Verified successfully")

    def test_class_group(self):
        """group 2"""
        # class group

        discriminant = -131653324254138636653163861414331698305531090221496467927360326686715180966094250598321899621249972220387687148397451395672779897144571112116763666653213748473909547482437246405018707472153290116227072825447643324530509016778432769802300913461285128339119844239772697652504835780459732685000796733645621728639
        a, b = 2, 1
        c = (b * b - discriminant) // (4 * a)
        group = ClassGroup(a, b, c, discriminant, self.T, 1024)
        vdf = VDF(group)
        self.assertTrue(testVDF(vdf, group))
        print("Verified successfully")

