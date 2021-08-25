"""
A Deck object contains a list of cards.  This class handles sorting and 
placing the raw word groups back into the deck and taking them out of the deck.
"""
import math

class Deck(object):
    def __init__(self, wordlist):
        self.wordlist = wordlist
        #print(self.wordlist)

    def getNextWord(self):
        '''Just pop off the word at the top of the <stack>.  Not really a stack though.'''
        return self.wordlist.pop(0)

    def placeWord(self, raw_word, percentage):
        '''Return a word back into the bag at a given percentage.  100% places it at the end.
        0% places it at the front.'''
        self.wordlist.insert(math.ceil(len(self.wordlist) * (percentage / 100.0)), raw_word)
