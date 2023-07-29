# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print( len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
global wordlist
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for char in secret_word:
        if char not in letters_guessed:
            return False
        
    return  True

    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_1 =  []
    
    
    for char in secret_word:
       
        if char in letters_guessed:
            
         word_1.append(char)
         
         
        else:
         word_1.append("_")  
        

    return ' '.join(word_1)





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
     
    word = (string.ascii_lowercase)
    x = list(word)
    word_copy = x[:]

    for char in word:
        if char in letters_guessed:
         word_copy.remove(char)
         
        else:
         word_copy
    
    return ''.join(word_copy)

   
    
    
def is_guess_valid(letter):
    
    return str.isalpha(letter)

def is_letter_guessed(secret_word,letter):
    
        if letter in secret_word:
            return True
        else:
            return False
    

# def available_guesses(guesses, get_available_letters(letters_guessed),secret_word):
#     guesses -= 1
#     if guesses > 0:
#        print('guesses_remaining: ' , guesses)
#        print("Remaining letters :" , get_available_letters(letters_guessed))
#     else:
#         print("Sorry you ran out of guesses. The word was : ", secret_word) 
#     return None
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.+
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of word that is" ,len(secret_word), "letters long.")
    print(f"You have {warnings} warnings left.")
    
#
    while   guesses > 0:
     print(f"you have {guesses} guesses left")
     print("Available letters :" , get_available_letters(letters_guessed))   
     letter = str.lower(input("Please guess a letter :",))
     if letter in letters_guessed:
         warnings -= 1
       
         if warnings >= 0:
            print(f"Oops! That letter is already guessed you have {warnings} warnings left ",get_guessed_word( secret_word , letters_guessed),"\n------------------------")
           
         else:
           guesses -= 1 
           if guesses > 0:
               print("Opps! you have already guessed that letter.you have no warnings left so you loose one guess : ",get_guessed_word( secret_word , letters_guessed),"\n------------------------")
           else:
               print("Sorry you ran out of guesses. The word was : ", secret_word)
  
     else:
         letters_guessed += letter
         
         if is_word_guessed(secret_word, letters_guessed) is True:
             print("Good guess : " , get_guessed_word( secret_word , letters_guessed) )
             print("congrat's you won ! ")
             break
         elif is_guess_valid(letter)is True:
              if is_letter_guessed(secret_word, letter) is True:
                  print("Good guess :", get_guessed_word( secret_word , letters_guessed),"\n-------------------------")
              
              else:
                  print("Opps That Letter is not in my word :", get_guessed_word( secret_word , letters_guessed),"\n-----------------------")
                  guesses -= 1
                  if guesses <= 0:
                      print("Sorry you ran out of guesses. The word was : ", secret_word)
                  
         else:
            warnings -= 1
            if warnings >= 0:
                print(f"Oops! Letter guessed is not valid. You have {warnings} warnings left : ",get_guessed_word(secret_word, letters_guessed))
            else:
              guesses -= 1 
              if guesses <= 0:
                print("Sorry you ran out of guesses. The word was : ", secret_word)
   
    return 
# secret_word = "apple"

# print(hangman(secret_word))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word1 = my_word.replace(" ","")
  
   # print(my_word2)
    if len(my_word1) !=len(other_word): return False
    for i in range (len(my_word1)):
           if my_word1[i] == "_":
               if other_word[i] in my_word: return False
           
           elif my_word1[i] != other_word[i]: return False
    return True
       
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
      
    possibilities = []
    for word in wordlist: 
      if match_with_gaps(my_word, word): 
        possibilities.append(word)
    return (' '.join(possibilities))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    warnings = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of word that is" ,len(secret_word), "letters long.")
    print(f"You have {warnings} warnings left.")
    
#
    while   guesses > 0:
     print(f"you have {guesses} guesses left")
     print("Available letters :" , get_available_letters(letters_guessed))   
     letter = str.lower(input("Please guess a letter :",))
     if letter == "*":
         print("possible word maches are : ",show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
     elif letter in letters_guessed:
         warnings -= 1
       
         if warnings >= 0:
            print(f"Oops! That letter is already guessed you have {warnings} warnings left ",get_guessed_word( secret_word , letters_guessed),"\n------------------------")
           
         else:
           guesses -= 1 
           if guesses > 0:
               print("Opps! you have already guessed that letter.you have no warnings left so you loose one guess : ",get_guessed_word( secret_word , letters_guessed),"\n------------------------")
           else:
               print("Sorry you ran out of guesses. The word was : ", secret_word)
  
     else:
         letters_guessed += letter
         
         if is_word_guessed(secret_word, letters_guessed) is True:
             print("Good guess : " , get_guessed_word( secret_word , letters_guessed) )
             print("congrat's you won ! ")
             break
         elif is_guess_valid(letter)is True:
              if is_letter_guessed(secret_word, letter) is True:
                  print("Good guess :", get_guessed_word( secret_word , letters_guessed),"\n-------------------------")
              
              else:
                  print("Opps That Letter is not in my word :", get_guessed_word( secret_word , letters_guessed),"\n-----------------------")
                  guesses -= 1
                  if guesses <= 0:
                      print("Sorry you ran out of guesses. The word was : ", secret_word)
                  
         else:
            warnings -= 1
            if warnings >= 0:
                print(f"Oops! Letter guessed is not valid. You have {warnings} warnings left : ",get_guessed_word(secret_word, letters_guessed))
            else:
              guesses -= 1 
              if guesses <= 0:
                print("Sorry you ran out of guesses. The word was : ", secret_word)
   
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
