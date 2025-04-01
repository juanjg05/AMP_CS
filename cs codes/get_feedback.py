import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
from valid_wordle_guesses import get_valid_wordle_guesses
from wordle_secret_words import get_secret_words
init(autoreset=True) #Ends color formatting after each print statement

'''from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses'''

def play_game():
    print('Hello! Welcome to Wordle! We have chosen a secret word and now you have six turns to guess it!!! \n:)')
    secrets = list(get_secret_words())
    secret_word = random.choice(secrets)
    print(secret_word)
    guesses_list = []

    for i in range(6):

        if i == 0:
            guess = input('Take a guess!\n')
            print(get_feedback(guess,secret_word))
            
        else:
            guess = input('Try again!\n')
            for each in guesses_list:
                print(each+'\n')

        guesses_list.append(get_feedback(guess,secret_word))
        
        if guess.upper() == secret_word:
            return "You got it!"

        



    
    #guess = input('')

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
    '''
    ### BEGIN SOLUTION
    feedback = ["-"]*5
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback[i] = secret_word[i].upper()
    for i in range(5):
        if not feedback[i].isalpha():
            for j in range(5):
                if guess[i] == secret_word[j]:
    '''
                    
    final = ['-']*5 #Back.WHITE + 

    if len(guess) != 5:
        return final
    
    secret = list(secret_word)
    guess = list(guess.upper())
    
    for i in range(len(guess)):    #LOOPS OVER ALL LETTERS IN GUESS LIST
        guessed_letter = guess[i]
        secret_letter = secret[i]
        yellow = guessed_letter.lower()

        if guessed_letter in secret or (guessed_letter + '?') in secret:
            print(guessed_letter)

            if guessed_letter in secret_letter:
                final[i] = guessed_letter #Back.GREEN
                secret[secret_word.index(guessed_letter)] = ''
                guess[guess.index(guessed_letter)] = ''
            
            elif guessed_letter in secret:
            
                final[i] = yellow #Back.YELLOW + Fore.BLACK+ 
                if secret_letter == guessed_letter:
                  secret[i] += '?'
                  guess[guess.index(guessed_letter)] = ''
        elif guessed_letter == secret_letter:
            guess[i] = ''
            secret[i]=''

        print(guessed_letter, final, secret, guess)
  
    for i in range (len(final)-1,0,-1):
        letter = final[i]
        inc_placed = letter.lower()
        freq_in_s = secret_word.count(letter.upper())
        freq_in_f = final.count(inc_placed) + final.count(letter.upper())
        if freq_in_f != freq_in_s and letter != letter.upper(): #If the lowercase count is not the same as the amount of the letter in the secret word
            final[i] = '-'
    
    return ''.join(final)
    
    # return ''.join(final)+Back.RESET




        # '''print(''.join(guess))
        #     print(''.join(secret))
        #     print(''.join(final))
        #     print('     ')'''

            
    return ''.join(final)+Back.RESET

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

    ### END SOLUTION 

# TODO: Define and implement your own functions!


if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    #pass
    print(get_feedback('OTOOM','MOOTO'))
    #print(play_game())
    #PA-Ss

