import math

def get_factors(n: int):
    '''Generates a sorted list of unique integer factors for a given natural number

        Args:
            n (int): The natural number which should be factored

        Returns:
            list: a list of unique integer factors in sorted order

        Examples:
            >>> get_factors(6)
            [1, 2, 3, 6]
            >>> get_factors(17)
            [1, 17]
            >>> get_factors(36)
            [1, 2, 3, 4, 6, 9, 12, 18, 36]
            >>> get_factors(-2)
            []
    '''
    ### BEGIN SOLUTION
    
    facts = []
    if n == 0 or n%1 != 0:
        return facts
    if n == 1:
        return [1]
    for i in range(1,(math.floor(n**.5))+1):
        if n%i == 0:
            facts.append(i)
    if facts[-1] == n/facts[-1]:
        for i in range(len(facts)-1,0,-1):
            facts.append(int(n/facts[i-1]))
    else:
        for i in range(len(facts),0,-1):
            facts.append(int(n/facts[i-1]))
    return facts
    
    ### END SOLUTION

def is_prime(n: int) -> bool:
    '''Determines whether a given integer is prime

       Args:
            n (int): The integer which should be tested

       Returns:
            bool: True if n is prime, False if n is not prime

       Examples:
            >>> is_prime(6)
            False
            >>> is_prime(11)
            True
    '''
    ### BEGIN SOLUTION
    if n%1 != 0:
        return False
    if n<=1:
        return False
    if n==2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(math.floor(n**.5)+2),2):
        if n%i ==0:
            return False
    return True

    ### END SOLUTION 

def largest_prime_factor(n: int) -> int:
    '''Determines the largest prime factor of a given whole number > 1.

       Args:
            n (int): The whole number which should be considered

       Returns:
            int: The largest prime factor of n
                 If the given integer isn't a whole number > 1, returns 0

       Examples:
            >>> largest_prime_factor(6)
            3
            >>> largest_prime_factor(100)
            5
    '''
    ### BEGIN SOLUTION
    if n%1 != 0 or n < 1:
        return 0
    else:
        flist = get_factors(n)
        plist = []
        for j in range(len(flist)):
            if is_prime(flist[j]):
                plist.append(flist[j])
    return plist[-1]

    

    ### END SOLUTION 

if __name__ == "__main__":
    print("get_factors(25): ", get_factors(12))
    print("is_prime(17): ", is_prime(3))
    print("largest_prime_factor(35): ", largest_prime_factor(600851475143))