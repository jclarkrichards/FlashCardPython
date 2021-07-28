from random import randint
import math
import os
from tkinter import *
from tktest import Example
from wordgroup import WordGroup

vocab = "Vocab/vocab.txt"    #words that have at least a 50% success rate
vocab_temp = "Vocab/temp.txt"

def fixVocabFiles():
    '''Make sure all lines have the 4 sections:  polish::english::right::wrong'''
    f = open(vocab, "r+", encoding='utf-8')
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
    f = open(vocab, "w+", encoding='utf-8')
    for line in newlines:
        f.write(line + "\n")
    f.close()
    

def readVocabFile(vocabfile):
    data = []
    with open(vocabfile, "r+", encoding='utf-8') as file:
        data = file.readlines()
    return data

def writeVocabFile(vocabfile, data):
    with open(vocabfile, "w+", encoding='utf-8') as file:
        file.writelines(data)

    
def generateRandomPack(num):
    '''Choose words randomly.  Remove chosen words from file and save into own file.'''
    words = readVocabFile(vocab)
    if len(words) < num:
        num = len(words)

    pack = []

    for i in list(range(num)):
        index = randint(0, len(words)-1)
        pack.append(words.pop(index))


    writeVocabFile(vocab_temp, pack)
    writeVocabFile(vocab, words) 
        
    return pack


def fileWordsToFiles(pack):
    '''For each entry in the pack, find the correctness or how well you know the word and file
    it into the appropriate file'''
    f = open(vocab, "a+", encoding='utf-8')
        
    for wordgroup in pack:
        f.write(wordgroup)
    f.close()

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
