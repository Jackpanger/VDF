from RSAGroup import *
from ClassGroup import *
from VDF import *
if __name__ == '__main__':
    # Test for RSA group
    bits = 2048
    T = 3000

    """group 1 """
    # RSA group
    # group = RSAGroup(T, bits)

    """group 2"""
    # class group
    discriminant = -131653324254138636653163861414331698305531090221496467927360326686715180966094250598321899621249972220387687148397451395672779897144571112116763666653213748473909547482437246405018707472153290116227072825447643324530509016778432769802300913461285128339119844239772697652504835780459732685000796733645621728639
    a, b = 2, 1
    c = (b * b - discriminant) // (4 * a)
    group = ClassGroup(a, b, c, discriminant, T, 1024)

    VDF = VDF(group)

    # prover
    # t = 2^T, y = x^{2^T}
    y = VDF.vdf_eval()  # send y to verifier
    print("y: " + str(y))

    # generate random l to prover
    l = group.random_l()
    print("l: " + str(l))

    # generate pi
    pi = VDF.vdf_prove(l)
    print("pi: " + str(pi))

    # verifier
    print("check: " + str(VDF.vdf_verify(pi, y)))


