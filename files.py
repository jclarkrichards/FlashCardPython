"""
Handle all of the file stuff.  Getting the files and saving files etc.
"""
from random import randint
import math
import os

class Files(object):
    def __init__(self):
        self.masterfile = "Vocab/vocab_master.txt"
        self.vocabfile = "Vocab/vocab.txt" 
        self.checkForDuplicates()
        self.mergeFiles()
        self.fixVocabFiles()

    def openFile(self, filename, mode="r+"):
        return open(filename, mode, encoding='utf-8')

    def writeData(self, data, filename):
        with self.openFile(filename, "w+") as file:
            file.writelines(data)

    def appendData(self, line, filename):
        f = self.openFile(filename, "a+")
        f.write(line)
        f.close()

    def mergeFiles(self):
        '''Any new words we added to the master file we also want to add to the vocab file.'''
        masterdata = self.openFile(self.masterfile)
        data = self.openFile(self.vocabfile)
        words = []
        for line in data:
            words.append(line.split("::")[0])
        for line in masterdata:
            if line.split("::")[0] not in words:
                self.appendData(line, self.vocabfile)

    def checkForDuplicates(self):
        '''Go through the master vocab file and check for duplicate words (in english)'''
        data = self.readVocabFile(self.masterfile)
        newdata = []
        temp = []
        for line in data:
            word = line.split("::")[0]
            if word not in temp:
                temp.append(word)
                newdata.append(line)
        self.writeData(newdata, self.masterfile)


    def sortVocabFile(self):
        '''Sort the master vocab file in alphabetical (english)'''
        pass

    def fixVocabFiles(self):
        '''Make sure all lines have the 5 sections:  polish::english::right::wrong::last::streak::decks'''
        #f = open(self.vocabfile, "r+", encoding='utf-8')
        f = self.openFile(self.vocabfile)
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
        #f = open(self.vocabfile, "w+", encoding='utf-8')
        f = self.openFile(self.vocabfile, "w+")
        for line in newlines:
            f.write(line + "\n")
        f.close()
    
    def readVocabFile(self, vocabfile):
        data = []
        with self.openFile(vocabfile) as file:
        #with open(vocabfile, "r+", encoding='utf-8') as file:
            data = file.readlines()
        return data

    #def writeVocabFile(self, vocabfile, data):
    #    with self.openFile(vocabfile, "w+") as file:
    #    #with open(vocabfile, "w+", encoding='utf-8') as file:
    #        file.writelines(data)
   
    def generateRandomPack(self, num):
        '''Choose words randomly.'''
        words = self.readVocabFile(self.vocabfile)
        
        if len(words) < num:
            num = len(words)

        maxvalue = self.getMaxDeckValue(words)
        words, used = self.filterMostUsed(words, maxvalue, num)

        pack = []

        for i in list(range(num)):
           index = randint(0, len(words)-1)
           pack.append(words.pop(index))

        #self.writeVocabFile(self.vocabfile, words) 

        self.writeData(words+used, self.vocabfile)
        
        return pack

    def getMaxDeckValue(self, words):
        '''return the maximum number of times a word has been added to a deck'''
        nums = []
        for word in words:
            nums.append(int(word.split("::")[6]))
        return max(nums)

    def filterMostUsed(self, words, maxvalue, num):
        temp = []
        used = []
        for word in words:
            val = int(word.split("::")[6])
            if val < maxvalue:
                temp.append(word)
            else:
                used.append(word)
        
        if len(temp) < num:
            return words, used
        return temp, used

    def fileWordsToFiles(self, pack):
        '''Send the temp words back to the vocab file'''
        #f = open(self.vocabfile, "a+", encoding='utf-8')    
        f = self.openFile(self.vocabfile, "a+")
        for card in pack:
            card.regroup()
            f.write(card.raw)
        f.close()