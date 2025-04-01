import random
# To install colorama, run the following command in your VS Code terminal:
#python3 -m pip install colorama

from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

'''from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses'''

def get_feedback(guess: str, secret_word: str) -> str:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word

        Returns:
            str: Feedback string, based on comparing guess with the secret word
    
        Examples
        >>> get_feedback("lever", "EATEN")
        "-e-E-"
            
        >>> get_feedback("LEVER", "LOWER")
                "L--ER"
            
        >>> get_feedback("MOMMY", "MADAM")
                "M-m--"
            
        >>> get_feedback("ARGUE", "MOTTO")
                "-----"

    
    '''
    ### BEGIN SOLUTION
    final = ['-']*5
    if len(guess) != 5:
        return final
    secret = list(secret_word)
    guess = list(guess.upper())
    for i in range(len(guess)):
        gletter = guess[i] #this is the letter you are guesing 
        #error when there isn't a letter
        if gletter in secret or gletter.lower() in secret:
            secret_count = secret.count(gletter)#HMMMMMMMMMMMMMMMMMM 
            final_count = final.count(gletter.lower()) + final.count(gletter.upper())#######HMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
            sletter = secret[i]
                                    #returns the first index of a thing, need it to return the i++ index
            if sletter.lower() == gletter.lower():
                final[i] = gletter.upper()
                secret.remove(gletter)
                secret.insert((i),' ')
                for z in final:
                    if gletter.lower() in final and gletter.upper() not in secret:
                        final.insert(final.index(gletter.lower()),'-')
                        final.remove(gletter.lower())
            if sletter.lower() != gletter.lower() and (gletter.lower() not in final or secret_count > final_count):
                final[i] = gletter.lower()
    return ''.join(final)
                #secret[secret.index(gletter)] = secret[secret.index(gletter)].lower()
'''
            print(''.join(guess))
            print(''.join(secret))
            print(''.join(final))
            print('     ')
'''
            #secret_word.replace(sletter,' ')


    ### END SOLUTION 

def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
        
        Args:
         guesses (list): A list of string guesses, which could be empty
         feedback (list): A list of feedback strings, which could be empty
         secret_words (set): A set of potential secret words
         valid_guesses (set): A set of valid AI guesses
        
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    ### BEGIN SOLUTION
    guessed_list = guesses
    for guess in guessed_list:
        get_feedback(guess, secret_words)


    ### END SOLUTION 

# TODO: Define and implement your own functions!


if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    #pass
    print(get_feedback('TOOTH','MOTTO'))
    #PA-Ss

