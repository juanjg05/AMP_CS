import math
from itertools import permutations

def is_prime(n: int):
    for i in range(3,int(math.floor(n**.5)+2),2):
        if n%i == 0:
            return False
    return True

def primenum():
    
    primes = [2, 3]
    start = primes[-1] +2
    while primes[-1]<4999:
        if is_prime(start):
            primes.append(start)
            start = primes[-1] + 2
        else:
            start = start +2

    return primes


if __name__ == '__main__':
    print(len(primenum()))
    print(math.ceil(math.log10(2**669)))
    #print(primenum())