import math
from itertools import permutations

def is_prime(n: int):
    if n%2 == 0:
        return False
    for i in range(3,math.ceil(n**.5),2):
        if n%i == 0:
            return False
    return True

def primenum(n: int):
    
    primes = [2,3]
    start = primes[-1] +2
    while len(primes)<n:
        if is_prime(start):
            primes.append(start)
            start = primes[-1] + 2
        else:
            start = start +2
    return primes[-1]

def pandig(n: tuple):
    number = 0
    for i in range(len(n)):
        number = number + n[i]*10**(len(n)-i-1)
    return number

def panlist(n: int):
    #n is the number of digits in the pandigital
    #got help from a ta with the permutations function

    list1 = [] #stop
    for i in range(1,n+1):
        list1.append(i)
    perm = permutations(list1)
    number = 0
    panprimes = []
    for i in list(perm):
        number = pandig(i)
        if is_prime(number):
            panprimes.append(number)
    return panprimes[-1]

if __name__ == "__main__":

    print(primenum(10001))
    print(panlist(7))