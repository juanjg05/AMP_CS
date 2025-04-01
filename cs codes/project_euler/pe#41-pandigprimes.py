import math
from itertools import permutations

def is_prime(n: int):
    if n%2 == 0:
        return False
    for i in range(3,math.ceil(n**.5),2):
        if n%i == 0:
            return False
    return True

def pandig(n: tuple):
    number = 0
    for i in range(len(n)):
        number = number + n[i]*10**(len(n)-i-1)
    return number
    

def panodds(n: int):
    #the last digit has to be 1, 3, 7 (not 5 bc no number past 5 ending with a 5 is prime. also not 9 bc if were looking for the largest I feel like it would start with 9)
    #largest pandigital in this case would be 987654321?

    list1 = [] #stop
    for i in range(1,n+1):
        list1.append(i) #[4,3,2,1] if n =4
    perm = permutations(list1)
    number = 0
    panprimes = []
    for i in list(perm):
        number = pandig(i)
        if is_prime(number):
            panprimes.append(number)
    return panprimes[-1]

if __name__ == "__main__":
    
    print(panodds(4))