import random


# Generate prime
def generate_prime(bits):
    while True:
        # p = random.randint(2 ** (bits - 1), 2 ** bits - 1)
        p = int('1' + ''.join(random.choices('01', k=bits - 2)) + '1', 2)
        if is_prime(p):
            return p


# Miller-Rabin prime test
def is_prime(n, rounds=40):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True



