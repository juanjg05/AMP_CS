import time
import random
from itertools import permutations
#from valid_anagame_words import get_valid_word_list
from AnagramExplorer import AnagramExplorer

def generate_letters(fun_factor: int, distribution: str, explorer:AnagramExplorer) -> list:
    '''Generates a list of 7 randomly-chosen lowercase letters which can form at least 
      fun_factor unique anagramable words

         Args:
          fun_factor (int): minimum number of unique anagram words offered by the chosen letters
          distribution (str): The type of distribution to use in order to choose letters
                            "uniform" - chooses letters based on a uniform distribution, with replacement
                            "scrabble" - chooses letters based on a scrabble distribution, without replacement
          explorer (AnagramExplorer): helper object used to facilitate computing anagrams based on specific letters.
         
         Returns:
             set: A set of 7 lowercase letters

         Example
         -------
         >>> explorer = AnagramExplorer(get_valid_word_list())
         >>> generate_letters(75, "scrabble", explorer)
         ["p", "o", "t", "s", "r", "i", "a"]
    '''
    letters = ["p", "o", "t", "s", "r", "i", "a"]  # Tip: Start with a consistent list of letters for testing purposes
    ### BEGIN SOLUTION

    uniform_let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    scrabble_let = ['a','a','a','a','a','a','a','a','a','b','b','c','c','d','d','d','d','e','e','e','e','e','e','e','e','e','e','e','e','f','g','h','f','g','h','g','i','i','i','i','i','i','i','i','i','j','k','l','m','l','m','l','l','n','o','n','o','n','o','n','o','n','o','n','o','o','o','p','p','q','r','r','r','r','r','r','s','t','u','s','t','u','s','t','u','s','t','t','t','u','v','w','v','w','x','y','y','z', ' ', ' ']
    scrabble_let.sort()
    fun = 0
    let = []
    #if distribution == "uniform":
    while fun != fun_factor:
            let.append(uniform_let[random.randint(0,25)])
            fun_factor = len(explorer.get_all_anagrams(self,let))
            if len(let) > 7:
                let.remove(let[0])
          
          
    '''elif distribution == "scrabble":
        while fun != fun_factor:
            let.append(uniform_let[random.randint(0,99)])
            fun_factor = len(explorer.get_all_anagrams(self,let))
            if len(let) > 7:
                let.remove(let[0])'''
    return let

    ### END SOLUTION 


def parse_guess(guess:str) -> tuple:
    '''Splits an entered guess into a two word tuple with all white space removed

        Args:
            guess (str): A single string reprsenting the player guess

        Returns:
            tuple: A tuple of two words. ("", "") in case of invalid input.

        Examples
        --------
        >>> parse_guess("eat, tea")
        ("eat", "tea")

        >>> parse_guess("eat , tea")
        ("eat", "tea")

        >>> parse_guess("eat,tea")
        ("eat", "tea")

        >>> parse_guess("eat tea")
        ("", "")
    '''
   ### BEGIN SOLUTION

    tup = tuple(guess.split(","))
    return tup

   ### END SOLUTION 

def play_game(time_limit: int, letters: list, explorer:AnagramExplorer) -> list:
    '''Plays a single game of AnaGame

       Args:
         time_limit: Time limit in seconds
         letters: A list of valid letters from which the player can create an anagram
         explorer (AnagramExplorer): helper object used to compute anagrams of letters.

       Returns:
          A list of tuples reprsenting all player guesses
   '''
    guesses = [] 
    quit = False

    start = time.perf_counter() #start the stopwatch (sec)
    stop = start + time_limit

    while time.perf_counter() < stop and not quit:
        guess = input('')
        if guess.strip() == "quit":
            quit = True
        elif guess.strip() == "hint":
            print(f"Try working with: {explorer.get_most_anagrams(letters)}")
        else:
          tuple_guess = parse_guess(guess)
          if len(tuple_guess[0]) > 1:
            guesses.append(tuple_guess)
          else:
            print("Invalid input")

        print(f"{letters} {round(stop - time.perf_counter(), 2)} seconds left")

    return guesses

def calc_stats(guesses: list, letters: list, explorer) -> dict:
    '''Aggregates several statistics into a single dictionary with the following key-value pairs:
        "valid" - list of valid guesses
        "invalid" - list of invalid/duplicate guesses
        "score" - per the rules of the game
        "accuracy" -  truncated int percentage representing valid player guesses out of all player guesses
                      3 valid and 5 invalid guesses would result in an accuracy of 37 --> 3/8 = .375
        "guessed" - set of unique words guessed from valid guesses
        "not guessed" - set of unique words not guessed
        "skill" - truncated int percentage representing the total number of unique anagram words guessed out of all possible unique anagram words
                  Guessing 66 out of 99 unique words would result in a skill of 66 --> 66/99 = .66666666
     Args:
      guesses (list): A list of tuples representing all word pairs guesses by the user
      letters (list): The list of valid letters from which user should create anagrams
      explorer (AnagramExplorer): helper object used to compute anagrams of letters.

     Returns:
      dict: Returns a dictionary with seven keys: "valid", "invalid", "score", "accuracy", "guessed", "not guessed", "skill"
    
     Example
     -------
     >>> letters = ["p", "o", "t", "s", "r", "i", "a"]
     >>> guesses = [("star","tarts"),("far","rat"),("rat","art"),("rat","art"),("art","rat")]
     >>> explorer = AnagramExplorer(get_valid_word_list())
     >>> calc_stats(guesses, letters, explorer)
     {
        "valid":[("rat","art")],
        "invalid":[("star","tarts"),("far","rat"),("rat","art"),("art","rat")],
        "score": 1,
        "accuracy": 20,
        "guessed": { "rat", "art" },
        "not_guessed": { ...73 other unique },
        "skill": 2
     }
    '''
    stats = {}
    stats["valid"] = []   #list of tuples
    stats["invalid"] = [] #list of tuples
    stats["score"] = 0    #total score per the rules of the game
    stats["accuracy"] = 0 #truncated int percentage representing valid player guesses out of all player guesses
    stats["skill"] = 0    #truncated int percentage representing unique guessed words out of all possible unique anagram words
    stats["guessed"] = set() #unique valid guessed words
    stats["not guessed"] = set() #unique words the player could have guessed, but didn’t
    ### BEGIN SOLUTION

    ### END SOLUTION 
    return stats

if __name__ == "__main__":
   print(generate_letters())