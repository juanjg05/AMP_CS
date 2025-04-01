import math

def words():
    txt = open("words.txt").read().split('","')
    txt[0] = txt[0][1::]
    txt[-1] = txt[-1][0:len(txt[-1])-1:]
    txt.sort(key=len)
    return txt

def squares(n: int):
    sq = []
    sqp = []
    for i in range(int(math.floor((10**(n-1))**.5)),int(math.ceil(10**(n))**.5)):
        sq.append(str(i**2))
    for i in sq:
        z = str(i)
        check1 = set(list(z))
        check2 = list(z)
        if len(check1) == len(check2):
            sqp.append(i)
        
    return sqp

prime_map = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11, 'F': 13,
    'G': 17, 'H': 19, 'I': 23, 'J': 29, 'K': 31, 'L': 37, 'M': 41, 'N': 43,
    'O': 47, 'P': 53, 'Q': 59, 'R': 61, 'S': 67, 'T': 71, 'U': 73, 'V': 79,
    'W': 83, 'X': 89, 'Y': 97, 'Z': 101, '1': 103, '2':107, '3':109, '4':113, '5':127, '6':131, '7':137,'8':139,'9':149,'0':151 }

def prime_hash(word: str):
  #calculates the prime hash value for a given word
  hash_value = 1
  for letter in word:
     hash_value *= prime_map[letter]
  return hash_value

def anagrams(corpus:list) -> dict:

        ### BEGIN SOLUTION

        keys = []

        dictionary = dict()

        for word in corpus:
          hash = prime_hash(word)
          if hash not in dictionary and len(word)>2:
              dictionary[hash] = [word]
          elif len(word)>2:
              dictionary[hash].append(word)

        for key in dictionary.keys():
          if len(dictionary[key]) > 1:
              keys += [key]
        
        ana_dict = dict()
        for key in keys:
            ana_dict[key] = dictionary[key]

        return ana_dict

#assign each anagramic word a point value from the anagramic square list and see if any of the anagrams match, if they don't go to the next anagramic square with the same length of the word 
#this is assuming word1 and word2 are already anagrams
#

def map_anagramic_squares(word1:str, word2:str):
    numDict = anagrams(squares(len(word1)))
    #print(numDict)
    finalll = []
    map1 = {}
    list1 = list(word1)
    for i in range(len(word1)):
        map1[list1[i]] = ""
    for val in numDict.values():
        numstr = ""
        for i in range(len(val[0])):
            map1[word1[i]] = val[0][i]
        for ch in word2:
            numstr += map1[ch]
        if numstr in val:
            finalll += val
    return (finalll,word1,word2)

def loop(words:dict):
    tup = tuple()
    maps = []
    for val in words.values():
        p1 = val[0]
        p2 = val[1]
        map = map_anagramic_squares(p1,p2)
        maps.append(map)
    final = []
    for i in maps:
        if i[0] != []:
            final.append(i)
        
    return final[-1]

def get_small():
    small = 0
    z = 0
    while small == 0:
        z +=20
        if z%11 == 0 and z%12 == 0 and z%13 == 0 and z%14 == 0 and z%15 == 0 and z%16 == 0 and z%17 == 0 and z%18 == 0 and z%19 == 0 and z%20 == 0:
            small = z
    return small

if __name__ == "__main__":
    print(get_small())
    print(loop(anagrams(words()))) #has to be 18769 because its the only number pair with 17689 where B = 1 is in the correct position
    