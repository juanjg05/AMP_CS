import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
from valid_wordle_guesses import get_valid_wordle_guesses
from wordle_secret_words import get_secret_words
init(autoreset=True) #Ends color formatting after each print statement

'''from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses'''

def is_valid_guess(guess: str) -> bool:

    guess = guess.upper()
    if len(guess) == 5 and guess in get_valid_wordle_guesses():
        return True
    return False

def color_correct(guess: str, get_feedback:str): #get_feedback is the get_feedback return

    guess = list(guess)
    get_feedback = list(get_feedback)
    
    for i in range(5):
        get = get_feedback[i]
        if get == '-':
            guess[i] = Back.LIGHTBLACK_EX + Fore.BLACK + guess[i].upper() + Back.RESET + Fore.RESET
        elif get in 'abcdefghijklmnopqrstuvwxyz':
            guess[i] = Back.LIGHTYELLOW_EX + Fore.BLACK + guess[i].upper() + Back.RESET + Fore.RESET
        elif get in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            guess[i] = Back.LIGHTGREEN_EX + Fore.BLACK + guess[i].upper() + Back.RESET + Fore.RESET

    return ''.join(guess) #checked and it works perfectly

def play_game():

    print('Hello! Welcome to Wordle! We have chosen a secret word and now you have six turns to guess it!!! \n:)')
    secrets = list(get_secret_words())
    secret_word = random.choice(secrets)
    #Back.LIGHTGREEN_EX + Fore.BLACK + random.choice(secrets) + Back.RESET + Fore.RESET
    guess_list = []
    #print(secret_word)

    guess = input('Take a guess!\n') # This is the first guess start
    print('-----')
    while False == (is_valid_guess(guess)):
        guess = input('Not a valid guess... Try again.........\n')
        print('-----')
    guess_list.append(guess.upper())
    guess_list.append(get_feedback(guess,secret_word))
    print(color_correct(guess_list[0],guess_list[1]))
    print('-----')
    if guess_list[1] == secret_word:
            return 'wohooo!!!!!!!!!!!!!!!! you dont suck at wordle!'
    #this is the first guess end

    for i in range(2,14,2): #this is a loop for rounds 2-6. If the person wins, or they don't get the word, then it breaks.

        if i > 11: #this is if they don't guess the word in 6 tries.
            for z in range(0,len(guess_list),2): #these for loops are to reprint the whole wordle square
                print(color_correct(guess_list[z],guess_list[z+1]))#printing color correct version of your guess
            print('-----')
            print('womp womp, you suck a guessing five letter words. The answer is ' + secret_word)
            break

        #if the wordle is correct!

        #if the wordle is wrong :(
        guess = input('Guess again!\n')
        print('-----')
        while is_valid_guess(guess) == False: #while loop to make sure that the guess isnt invalid
            guess = input('Invalid... Guess again...\n')
        guess_list.append(guess.upper())
        guess_list.append(get_feedback(guess,secret_word))

        if guess_list[i+1] != secret_word: #guess_list[i+1] == get_feedback string
            for z in range(0,len(guess_list),2): #reprint wordle
                print(color_correct(guess_list[z],guess_list[z+1]))#printing color correct version of your guess
            print('-----')
            print("Looks like this isn't the right word either...")
        elif guess_list[i+1] == secret_word: #guess_list[i+1] == get_feedback string
            for z in range(0,len(guess_list),2):
                print(color_correct(guess_list[z],guess_list[z+1]))#printing color correct version of your guess
            print('-----')
            print('wohooo!!!!!!!!!!!!!!!! you dont suck at wordle!')
            return guess_list[z+1]
            break
    
    return ''

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
    ### BEGIN SOLUTION

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
            #print(guessed_letter)

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

        #print(guessed_letter, final, secret, guess)
  
    for i in range (len(final)-1,0,-1):
        letter = final[i]
        inc_placed = letter.lower()
        freq_in_s = secret_word.count(letter.upper())
        freq_in_f = final.count(inc_placed) + final.count(letter.upper())
        if freq_in_f != freq_in_s and letter != letter.upper(): #If the lowercase count is not the same as the amount of the letter in the secret word
            final[i] = '-'
    
    return ''.join(final)

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

    
    #initial can be audio since it has three vowels and an s
    #if first guess is all black
        # is second guess, checks all vowels and also checks new cosonants (word that isn't vowel)
        #if second guess is all black
            #nymph would be the third since it uses completely different letters

    #for every guess, log its letters and position

        #coding - make a difference between correct and wrong position.

        #if letter is wrong (so if it prints as grey or '-')
            #skip every word in valid_wordle_guesses with that letter
        #if position is wrong (so if it prints yellow or lowercase)
            #skip any word with that letter in that position
        #if position and letter are right
            #skip any word without that letter in that position.
            #find words that haven't been deleted with letters in that position

    if len(guesses) == 0:
        return 'ROATE'
    if feedback[0] == '-----':
        return 'JUICY'
    
    
    

    
    
    f#or guess in guesses:
        
    


    

    
    
 

    ### END SOLUTION 

# TODO: Define and implement your own functions!


if __name__ == "__main__":
    # TODO: Write your own code to call your functions here
    #pass
    #print(get_feedback('MOWER','ORDER')) this can be improved
    #print(color_correct('MOWER','-o-ER')) this seems to work in all scenerios
    print(play_game())
    #PA-Ss

