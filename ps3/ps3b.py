from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    perm = []

    sum = 0
    for i in hand:
        sum += hand[i]

    for i in range(1, sum+1):
        perm.extend(get_perms(hand, i))

    max = ["", 0]
    for i in perm:
        if i in word_list:
            score = get_word_score(i, HAND_SIZE)
            if score > max[1]:
                max = [i, score]

    if max[0] == "":
        return False
    else:
        return max[0]

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    totalScore = 0
    print "The computer has a hand of:",
    while True:
        display_hand(hand)
        word = comp_choose_word(hand, word_list)
        if word != False:
            update_hand(hand, word)
            score = get_word_score(word, HAND_SIZE)
            totalScore += score
            print "The computer chooses the word", word, "with a score of", score
        else:
            print "The computer ends their turn with a total score of", totalScore
            break
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    pInput = ""
    pInput2 = ""

    score = 0

    hand = {}
    prevHand = {}

    while pInput != "e":
        pInput = raw_input("Enter \"n\" to play a new hand, \"r\" to play the previous hand, or \"e\" to exit: ")
        pInput = pInput.lower()
        if pInput == "n":
            hand = deal_hand(HAND_SIZE)
            prevHand = hand.copy()
            cHand = hand.copy()
            score += play_hand(hand, word_list)
        elif pInput == "r":
            if prevHand == "":
                print "You don't have a previous hand."
            else:
                score += play_hand(prevHand, word_list)
        elif pInput == "e":
            break
        else:
            print "That's not a valid input. Please try again."
            continue
        print "Grand total score:", score
        while True:
            pInput2 = raw_input("Enter \"u\" to play again or enter \"c\" to let a computer play a hand: ")
            pInput2 = pInput2.lower()
            print pInput2
            if pInput2 == "u":
                break
            elif pInput2 == "c":
                comp_play_hand(cHand, word_list)
                break
            else:
                print "That was an incorrect input. Please try again."
        

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    
