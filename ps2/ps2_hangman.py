# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

word = choose_word(wordlist)
word_len = len(word)
correct_guesses = 0
correct = ()
for i in range(0,word_len):
    correct += ('_',)
num_guess = 10
win = False
available = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def disp_word():
    global correct
    str = ""
    for i in range(0, word_len):
        str += correct[i]
    return str

def check(letter):
    newCorrect = ()
    state = False
    global correct
    global correct_guesses
    for i in range(0, len(word)):
        if word[i] == letter:
            newCorrect += (letter,)
            state = True
            correct_guesses += 1
        else:
            newCorrect += (correct[i],)
    
    correct = newCorrect
    
    return state

def check_avail(letter):
    newAvail = ()
    state = False
    global available
    for i in range(0, len(available)):
        if letter == available[i]:
            state = True
        else:
            newAvail += (available[i],)
    available = newAvail
    return state

def disp_avail():
    str = ""
    for i in range(0, len(available)):
        str += available[i]
    return str

print "Welcome to Hangman"
print "I'm thinking of a word with " + str(word_len) + " letters." 

while (win != True and num_guess > 0 and correct_guesses < word_len):
    print '------------------'
    print 'You have ' + str(num_guess) + ' guesses left.'
    print 'Available letters: ' + disp_avail()
    guess = raw_input('Please guess a letter:').lower()
    if check_avail(guess):
        if check(guess):
            print "Good guess: " + disp_word()
        else:
            num_guess -= 1
            print "Oops! That letter is not in my word: " + disp_word()
    else:
        print "You have already guessed " + guess

if num_guess <= 0:
    print "You were so close! The word was " + word
else:
    print "Congratulations, you won!"
