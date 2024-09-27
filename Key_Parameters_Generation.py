import random
from Database_Operations import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi



def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def generate_key_pair(p, q, r):
    if not (is_prime(p) and is_prime(q) and is_prime(r)):
        raise ValueError('All numbers must be prime.')
    if p == q or q == r or p == r:
        raise ValueError('All primes must be distinct')

    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    store_key_params(p, q, r, n, phi, e, d)

if __name__ == '__main__':


    generate_key_pair(17976934933339, 17976934933393, 17976934933403 )






