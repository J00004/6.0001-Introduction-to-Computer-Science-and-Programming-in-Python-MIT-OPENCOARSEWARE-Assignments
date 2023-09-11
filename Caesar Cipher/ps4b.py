# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return self.message_text
         #delete this line and replace with your code here

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        self.valid_words = self.valid_words.copy()
        return self.valid_words
        

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
         
        dict_shift = {}
        Alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for idx , i  in enumerate(Alphabet):
               if idx + shift <52:
                    if i == i.upper():
                        dict_shift[i] = Alphabet [idx + shift].upper()
                    else:
                        dict_shift[i] = Alphabet [idx + shift].lower()
                        
               else:
                    if i == i.upper():
                        dict_shift[i] = Alphabet [idx+shift-52 ].upper()
                    else:
                        dict_shift[i] = Alphabet [idx+shift-52 ].lower()
            
        return dict_shift

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dict_shift = Message.build_shift_dict (self,shift)
        message_text = self.get_message_text()
        shifted_chars = ''
        for i in message_text:
            if i.isalpha() is True :
                shifted_chars +=  dict_shift[i]
                
            else:  
                shifted_chars += i
                  
        return shifted_chars

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
      
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift 

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        self.encryption_dict = self.encryption_dict.copy()
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        shifts = 26
        best_shifts = None
        valid_messages = ""
        max_num_valid_words = 0
        # valid = list(valid_messages)
        # best = list(best_shifts)
        plaintext = PlaintextMessage(self.get_message_text(), 0)
        for shift in range(shifts):
            valid_words = 0
            plaintext.change_shift(shift)
            decripted_message = plaintext.get_message_text_encrypted()
            decripted_words = decripted_message.split(" ")
         
           
            for word in decripted_words:
                if is_word(self.valid_words, word) is True:
                    valid_words+=1
                    
                if is_word(self.valid_words, word) is True:
                    valid_words +=1
            if valid_words>max_num_valid_words:
                max_num_valid_words = valid_words
                valid_messages = decripted_message
                best_shifts = shift
            
        return (best_shifts,valid_messages.strip())

if __name__ == '__main__':
     # a = Message("cat")
     # print(a.get_message_text())
     # print(a.build_shift_dict(5))
     # print(a.apply_shift(5))
     plaintext = PlaintextMessage("i am jayesh",4)
     print('Expected Output: "m eq ncamsi"')
     print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
     ciphertext = CiphertextMessage('jgnnq')
     print('Expected Output:', (24, 'hello'))
     print('Actual Output:', ciphertext.decrypt_message())
def test_plaintext():
    plain_1 = PlaintextMessage('hello', 2)
    plain_2 = PlaintextMessage('hello', 1)
    plain_3 = PlaintextMessage('Lali says Hello!!', 4)
    plain_4 = PlaintextMessage('I love cats. Do you?', 6)

    exp_1 = 'jgnnq'
    exp_2 = 'ifmmp'  
    exp_3 = 'Pepm wecw Lipps!!' 
    exp_4 = 'O rubk igzy. Ju eua?'

    test_1 = plain_1.get_message_text_encrypted() == exp_1
    test_2 = plain_2.get_message_text_encrypted() == exp_2
    test_3 = plain_3.get_message_text_encrypted() == exp_3
    test_4 = plain_4.get_message_text_encrypted() == exp_4
    
    if not test_1: print('FAILED: PlaintextMessage(hello, 2) did not return ' + exp_1)
    if not test_2: print('FAILED: PlaintextMessage(hello, 1) did not return ' + exp_2)
    if not test_3: print('FAILED: PlaintextMessage(Lali says Hello!!, 4) did not return ' + exp_3)
    if not test_4: print('FAILED: PlaintextMessage(I love cats, 6) did not return ' + exp_4)
    if test_1 and test_2 and test_3 and test_4:
        print('ALL PLAINTEXT TESTS PASSED. NICE!!')

def test_ciphertext():
    cipher_1 = CiphertextMessage('jgnnq')
    cipher_2 = CiphertextMessage('ifmmp')
    cipher_3 = CiphertextMessage('Pepm wecw Lipps!!' )
    cipher_4 = CiphertextMessage('O rubk igzy. Ju eua?')

    exp_1 = (26-2, 'hello')
    exp_2 = (26-1, 'hello')
    exp_3 = (26-4, 'Lali says Hello!!')
    exp_4 = (26-6, 'I love cats. Do you?')

    test_1 = cipher_1.decrypt_message() == exp_1
    test_2 = cipher_2.decrypt_message() == exp_2
    test_3 = cipher_3.decrypt_message() == exp_3
  
    test_4 = cipher_4.decrypt_message() == exp_4
    print( cipher_3.decrypt_message())
    print(cipher_4.decrypt_message())
    
    if not test_1: print('FAILED: CiphertextMessage(jgnnq) did not return ' + str(exp_1))
    if not test_2: print('FAILED: CiphertextMessage(ifmmp) did not return ' + str(exp_2))
    if not test_3: print('FAILED: CiphertextMessage(Pepm wecw Lipps!!) did not return ' + str(exp_3))
    if not test_4: print('FAILED: CiphertextMessage(O rubk igzy. Ju eua?) did not return ' + str(exp_4))
    if test_1 and test_2 and test_3 and test_4:
        print('ALL CIPHERTEXT TESTS PASSED. NICE!!')

test_plaintext()
test_ciphertext()
    
plain_text = PlaintextMessage("Password : Mandalorian", 17)
encrypted_message = plain_text.get_message_text_encrypted()
print(encrypted_message)

cipher_text = CiphertextMessage("Grjjnfiu : Dreurcfizre")
decrypted_message = cipher_text.decrypt_message()
print(decrypted_message)
   
