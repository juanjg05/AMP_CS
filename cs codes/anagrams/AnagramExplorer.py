prime_map = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def prime_hash(word: str):
  #calculates the prime hash value for a given word
  hash_value = 1
  for letter in word:
     hash_value *= prime_map[letter]
  return hash_value

def lower_case(word1):
    word_1 = list(word1.lower())
    for i in word_1:
        if i.isalpha() == False:
            word_1.remove(i)
    return "".join(word_1)

class AnagramExplorer:
    def __init__(self, all_words: list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.build_lookup_dict() # Only calculated once, when the explorer object is created

    @property
    def corpus(self):
      return self.__corpus

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str]) -> bool:
         '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)
            -are both at least 3 letters long (and the same)
            -form a valid anagram pair
            -???????????????consist entirely of letters chosen at the beginning of the game
            Args:
                pair (tuple): Two strings representing the guessed pair
                letters (list): A list of letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
         '''
         ### BEGIN SOLUTION

         word1 = lower_case(pair[0])
         word2 = lower_case(pair[1])
         letters1 = "".join(letters)
         if len(word1)<3 or len(word2)<3 or len(word1)!=len(word2) or word1 == word2:
             return False
         if word1 not in self.corpus or word2 not in self.corpus:
             return False
         num1 = prime_hash(word1)
         num2 = prime_hash(word2)
         lethash = prime_hash(letters1)
         if lethash%num1 != 0 or lethash%num2 != 0:
             return False
         if num1 == num2:
             return True
         return False

        ### END SOLUTION 
        
    def build_lookup_dict(self) -> dict:
        '''Creates a fast dictionary look-up (via either prime hash or sorted tuple) of all anagrams in a word corpus.
       
            Args:
                corpus (list): A list of words which should be considered

            Returns:
                dict: Returns a dictionary with  keys that return sorted lists of all anagrams of the key (per the corpus)
        '''
        ### BEGIN SOLUTION
        corpus = self.__corpus
        corpus.sort()
    
        diction1 = dict()

        for word in corpus:
          hash = prime_hash(word)
          if hash not in diction1:
              diction1[hash] = [word]
          else:
              diction1[hash].append(word)
        return diction1
        ### END SOLUTION 

    def get_all_anagrams(self, letters: list[str]) -> set:
        '''Creates a set of all unique words that could have been used to form an anagram pair.
           Words which can't create any anagram pairs should not be included in the set.

            Ex)
            corpus: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
            all_anagrams: {"abed",  "abled", "baled", "bead", "blade"}

            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              set: all unique words in corpus which form at least 1 anagram pair
        '''
        ### BEGIN SOLUTION

        total_set = set()


        lhash = prime_hash("".join(letters))
        lookup_dict = self.anagram_lookup

        for key in lookup_dict.keys():
            if lhash%key==0 and len(lookup_dict[key])>1:
                for word in lookup_dict[key]:
                    total_set.add(word)
                
            
        return total_set

        ### END SOLUTION Correct : [ _ _ A _ _ ] Almost: 'S'

    def get_most_anagrams(self, letters:list[str]) -> str:
        '''Returns any word from one of the largest lists of anagrams that 
           can be formed using the given letters.
           
            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              str: a single word from the largest anagram families
        '''
        ### BEGIN SOLUTION
        dictionary = self.anagram_lookup

        str = ''
        length = 2
        lhash = prime_hash(''.join(letters))

        for words in dictionary.values():
            check = len(words)
            hash = prime_hash(words[0])
            if length == check and words[0] in self.corpus and len(words[0])>2 and lhash%hash == 0:
                str = words[0]
            elif check > length and words[0] in self.corpus and len(words[0])>2 and lhash%hash == 0:
                length = check
                str = words[0]

        return str
            
        ### END SOLUTION 

if __name__ == "__main__":
  words1 = [
     "abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
     "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
     "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"
  ]
  words2 = ["rat", "mouse", "art", "tar", "chicken", "stop", "pots", "tops" ]

  letters = ["l", "o", "t", "s", "r", "i", "a"]

  my_explorer = AnagramExplorer(words2)

  print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_all_anagrams(letters))