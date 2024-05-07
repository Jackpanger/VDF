from RSAGroup import *
from VDF import *
if __name__ == '__main__':
    # Test for RSA group
    bits = 2048
    T = 3000

    # RSA group
    rsa = RSAGroup(T, bits)
    VDF = VDF(rsa)

    # prover
    # t = 2^T, y = x^{2^T}
    y = VDF.vdf_eval()  # send y to verifier
    print("y: " + str(y))

    # generate random l to prover
    l = VDF.random_l(bits)
    print("l: " + str(l))

    # generate pi
    pi = VDF.vdf_prove(l)
    print("pi: " + str(pi))

    # verifier
    print("check: " + str(VDF.vdf_verify(pi, y)))











    # # RSA group
    # x, N = RSAGroup().setup(bits)
    #
    # # prover
    # # t = 2^T, y = x^{2^T}
    # prover = RSAProver(x, T, N)
    #
    # y = prover.vdf_eval()  # send y to verifier
    # print("y: " + str(y))
    #
    # # generate random l to prover
    # verifier = RSAVerifier(x, T, N)
    # l = verifier.random_l(bits)
    # print("l: " + str(l))
    #
    # # generate pi
    # pi = prover.vdf_prove(l)
    # print("pi: " + str(pi))
    #
    # # verifier
    # print("check: " + str(verifier.vdf_verify(pi, y)))
