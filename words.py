"""
A Deck object contains a list of cards.  This class handles sorting and 
placing the raw word groups back into the deck and taking them out of the deck.
"""
import math
from wordgroup import Card

class Deck(object):
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.cardList = []
        #print(self.wordlist)
        self.setup()

    def setup(self): 
        '''Create the cards from the words'''
        for word in self.wordlist:
            card = Card(word)
            card.decks_added += 1
            self.cardList.append(card)

    def getNextWord(self):
        '''Just pop off the word at the top of the <stack>.  Not really a stack though.'''
        return self.cardList.pop(0)

    def placeWord(self, card, percentage):
        '''Return a card back into the bag at a given percentage.  100% places it at the end.
        0% places it at the front.'''
        self.cardList.insert(math.ceil(len(self.cardList) * (percentage / 100.0)), card)
