import itertools

from itertools import permutations

def basic_checks(word1:str, word2:str)-> tuple[bool, str, str]:
    '''Implements top-level checks common to each is_anagram approach. 
       Anagram basic checks include ensuring the two input words:
        -aren't be the same word
        -are case insensitive
        -don't include characters other than A-Z, a-z
        -have the same length, with at least two letters

       Args:
         word1: The first word
         word2: The second word

       Returns:
         bool: False if the two words fail a basic check, True otherwise
         str: A lowercase version of word1 only containing A-Z, a-z
         str: A lowercase version of word2 only containing A-Z, a-z
        
       Examples:
        >>> basic_checks("baste2", "Beast")
        True, baste, beast
        >>> basic_checks("baste", "Beasts")
        False, baste, beasts
    '''
    ### BEGIN SOLUTION

    word_1 = list(word1.lower())
    word_2 = list(word2.lower())
    for i in word_1:
        if i.isalpha() == False:
            word_1.remove(i)
    for i in word_2:
        if i.isalpha() == False:
            word_2.remove(i)
    s = ""
    word1 = s.join(word_1)
    word2 = s.join(word_2)
    if word1 == word2:
        return (False, word1, word2)
    if len(word1) != len(word2):
        return (False, word1, word2)
    return (True, word1, word2)

    ### END SOLUTION 

def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    a,word1,word2 = basic_checks(word1,word2)
    if a == False:
        return False
    
    perm = permutations(word1)
    for i in perm:
        if i == tuple(word2):
            return True
    return False

def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION

    a,word1,word2 = basic_checks(word1,word2)
    if a == False:
        return False

    list1 = list(word1)
    list2 = list(word2)
    list2.append("") #had to add this because my nested for loop wouldn't run unless I made len -1, but then it wouldn't read the last letter and check off.
    
    for i in list1:
        for z in range(len(list2)-1):
            if i == list2[z]:
                list2.remove(list2[z])
                z = len(list2)
    if list2 == [""]:
        return True
    
    return False

    ### END SOLUTION 

def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''Two approaches:
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. chr(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    a,word1,word2 = basic_checks(word1,word2)
    if a == False:
        return False

    list1 = list(word1)
    list2 = list(word2)

    letter1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
    'w': 0, 'x': 0, 'y': 0, 'z': 0 }
    letter2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
    'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
    'w': 0, 'x': 0, 'y': 0, 'z': 0 }

    for i in list(list1):
        letter1[i] = letter1[i]+1
    for i in list(list2):
        letter2[i] = letter2[i]+1
    if letter1 == letter2:
        return True
    return False
    
    ### END SOLUTION 

def is_anagram_sort_hash(word1:str, word2:str)->bool:
    '''Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    
    a,word1,word2 = basic_checks(word1,word2)
    if a == False:
        return False

    list1 = list(word1)
    list2 = list(word2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False

    ### END SOLUTION 

ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def is_anagram_prime_hash(word1:str, word2:str)->bool:
    '''Create a dictionary of prime numbers (see chToprime above). Use the ascii value of each letter in both
      words to construct a unique numeric representation of the word (called a 'hash').
      Words with the same hash value are anagrams of each other.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    a,word1,word2 = basic_checks(word1,word2)
    if a == False:
        return False

    num1 = 0
    num2 = 0
    
    list1 = list(word1)
    list2 = list(word2)

    for i in list(list1):
        if i == list1[0]:
            num1 = ch_to_prime[i]
        else:
            num1 = num1*ch_to_prime[i]
    for i in list(list2):
        if i == list2[0]:
            num2 = ch_to_prime[i]
        else:
            num2 = num2*ch_to_prime[i]
    if num1 == num2:
        return True
    return False
    

    ### END SOLUTION 

if __name__ == "__main__":
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort_hash, is_anagram_prime_hash]
    word1 = "beast"
    word2 = "baste"
    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")