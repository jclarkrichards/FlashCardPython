"""
Handle all of the file stuff.  Getting the files and saving files etc.
"""
from random import randint
import math
import os
from tkinter import *
from tktest import Example
from wordgroup import WordGroup

class Files(object):
    def __init__(self):
        self.vocabfile = "Vocab/vocab.txt"    
        #self.tempfile = "Vocab/temp.txt"
        self.fixVocabFiles()

    def fixVocabFiles(self):
        '''Make sure all lines have the 5 sections:  polish::english::last::right::wrong'''
        f = open(self.vocabfile, "r+", encoding='utf-8')
        newlines = []
        for line in f:
            temp = line.split('\n')[0]
            newline = temp.split("::")
            if len(newline) == 2:
                temp += "::0::0::0::"
                #temp = newline[1]+"::"+newline[0]
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
        '''Choose words randomly.  Remove chosen words from file and save into own file.'''
        words = self.readVocabFile(self.vocabfile)
        if len(words) < num:
            num = len(words)

        pack = []

        for i in list(range(num)):
            index = randint(0, len(words)-1)
            pack.append(words.pop(index))


        #self.writeVocabFile(self.tempfile, pack)
        self.writeVocabFile(self.vocabfile, words) 
        
        return pack


    def fileWordsToFiles(self, pack):
        '''Send the temp words back to the vocab file'''
        f = open(self.vocabfile, "a+", encoding='utf-8')
        
        for wordgroup in pack:
            f.write(wordgroup)
        f.close()

  






"""
    #This is the start of the program
    fixVocabFiles()
    print("Welcome to Flash Learn.  Please select an option below")
    selection = -1

while selection != '3' and selection != 'q':
    print("Please make a selection from the following")
    print("1: Random Pack")
    print("2: Add Card")
    print("3 or q: QUIT")
    
    selection = input("Selection: " )

    if selection == '1':
        numwords = int(input("How many words to learn? " ))
        pack = generateRandomPack(numwords)
        root = Tk()
        test = Example(pack)
        root.mainloop()
        fileWordsToFiles(pack)

        
    elif selection == '2':  #Add a new entry
        word_eng = input("English: " )
        word_pol = input("Polish: ")
        #Should check for duplicates in case word already exists
        with open(vocab_new, "r+", encoding='utf-8') as file:
            data = file.readlines()
        canadd = True
        for line in data:
            if line.split("::")[0] == word_eng:
                canadd = False
                break
            
        if canadd:
            f = open(vocab_new, "a+", encoding='utf-8')
            word = WordGroup()
            f.write(word.group(word_eng, word_pol))
            f.close()


print("See ya next time!")
"""
