"""
Handle all of the file stuff.  Getting the files and saving files etc.
"""
from random import randint
import math
import os
#from tkinter import *
#from tktest import Example
#from wordgroup import Card

class Files(object):
    def __init__(self):
        self.masterfile = "Vocab/vocab_master.txt"
        self.vocabfile = "Vocab/vocab.txt"    
        self.fixVocabFiles()

    def mergeFiles(self):
        '''Merge the masterfile with the vocabfile'''
        pass

    def checkForDuplicates(self):
        '''Go through the master vocab file and check for duplicate words (in english)'''
        pass

    def sortVocabFile(self):
        '''Sort the master vocab file in alphabetical (english)'''
        pass

    def fixVocabFiles(self):
        '''Make sure all lines have the 5 sections:  polish::english::right::wrong::last::streak::decks'''
        f = open(self.vocabfile, "r+", encoding='utf-8')
        newlines = []
        for line in f:
            temp = line.split('\n')[0]
            newline = temp.split("::")
            if len(newline) == 2:
                temp += "::0::0::0::0::0::"
                newlines.append(temp)
            else:
                newlines.append(temp)
              
        f.close()
        #write changes back to file
        f = open(self.vocabfile, "w+", encoding='utf-8')
        for line in newlines:
            f.write(line + "\n")
        f.close()
    
    def readVocabFile(self, vocabfile):
        data = []
        with open(vocabfile, "r+", encoding='utf-8') as file:
            data = file.readlines()
        return data

    def writeVocabFile(self, vocabfile, data):
        with open(vocabfile, "w+", encoding='utf-8') as file:
            file.writelines(data)
   
    def generateRandomPack(self, num):
        '''Choose words randomly.'''
        words = self.readVocabFile(self.vocabfile)
        if len(words) < num:
            num = len(words)

        pack = []

        for i in list(range(num)):
            index = randint(0, len(words)-1)
            pack.append(words.pop(index))

        self.writeVocabFile(self.vocabfile, words) 
        
        return pack

    def fileWordsToFiles(self, pack):
        '''Send the temp words back to the vocab file'''
        f = open(self.vocabfile, "a+", encoding='utf-8')       
        for card in pack:
            f.write(card)
        f.close()