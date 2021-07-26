from random import randint
import math
import os
from tkinter import *
from tktest import Example

#3 files helps us keep track of which words we know, which ones we are struggling with
#and which ones are on neither side
#vocab_bad = "Vocab/vocab_bad.txt"    #words that have at least a 50% fail rate
vocab = "Vocab/vocab.txt"    #words that have at least a 50% success rate
#vocab_good = "Vocab/vocab_good.txt"  #words that are in between the two rates above
#vocab = [vocab_bad, vocab_new, vocab_good] #for looping
vocab_temp = "Vocab/temp.txt"

def fixVocabFiles():
    '''Make sure all lines have the 4 sections:  polish::english::right::wrong'''
    #for vfile in vocab:
    #print(vfile)
    f = open(vocab, "r+", encoding='utf-8')
    newlines = []
    for line in f:
        temp = line.split('\n')[0]
        newline = temp.split("::")
        if len(newline) == 2:
            temp += "::0::0::0::"
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

    #f = open(vocabfile, "r+")
    #wordlist = []
    #for line in f:
    #    wordlist.append(line.split('\n')[0])
              
    #f.close()
    #return wordlist

def writeVocabFile(vocabfile, data):
    with open(vocabfile, "w+", encoding='utf-8') as file:
        file.writelines(data)

    
def generateRandomPack(num):
    #words_bad = readVocabFile(vocab_bad)
    words = readVocabFile(vocab)
    #words_good = readVocabFile(vocab_good)
    if len(words) < num:
        #if (len(words_bad) + len(words_new) + len(words_good)) < num:
        #num = len(words_bad) + len(words_new) + len(words_good)
        num = len(words)

    #how many words should we extract from each file?
    #numgood = min(math.floor(num * 0.2), len(words_good))
    #numbad = min(math.floor(num * 0.3), len(words_bad))
    #numnew = min(num - numgood - numbad, len(words_new))
    #numnew = math.floor(num * 0.5)
    #print("Total = " + str(num))
    #print("Bad = " + str(numbad))
    #print("New = " + str(numnew))
    #print("Good = " + str(numgood))
    #We need to make sure each file has the necessary amount of words.
    #If not, then we'll need to get the words from another file
    #For example, in the beginning there will only be words in the words_new file
    #The other 2 files will be empty

    pack = []
    #indices = list(range(len(wordlist)))


    #for i in list(range(numgood)):
    #    index = randint(0, len(words_good)-1)
    #    pack.append(words_good.pop(index))

    #for i in list(range(numbad)):
    #    index = randint(0, len(words_bad)-1)
    #    pack.append(words_bad.pop(index))

    for i in list(range(num)):
        index = randint(0, len(words)-1)
        pack.append(words.pop(index))


    writeVocabFile(vocab_temp, pack)
    #writeVocabFile(vocab_good, words_good)
    #writeVocabFile(vocab_bad, words_bad)
    writeVocabFile(vocab, words) 
        
    return pack


def fileWordsToFiles(pack):
    '''For each entry in the pack, find the correctness or how well you know the word and file
    it into the appropriate file'''
    #fbad = open(vocab_bad, "a+", encoding='utf-8')
    #fgood = open(vocab_good, "a+", encoding='utf-8')
    f = open(vocab, "a+", encoding='utf-8')
    #print("Pack has " + str(len(pack)) + " words")
    
        
    for wordgroup in pack:
        f.write(wordgroup)
        '''
        right = int(wordgroup.split("::")[2])
        wrong = int(wordgroup.split("::")[3])
        #print(wordgroup)
        
        if right != 0 or wrong != 0:
            value = (right - wrong) / (right + wrong)
            print(value)
            if value >= 0.35:
                fgood.write(wordgroup)
            elif value <= -0.35:
                fbad.write(wordgroup)
            else:
                fnew.write(wordgroup)
            
        else:
            fnew.write(wordgroup)
        '''
    #fbad.close()
    #fgood.close()
    f.close()
    #os.remove(vocab_temp)
            


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
        #print(pack)
        #print(type(pack))
        #print(pack)
        #learning = True
        #numcorrect = 0
        root = Tk()
        test = Example(pack)
        root.mainloop()
        #print("Finished learning")
        #print(pack)
        fileWordsToFiles(pack)
        
    if selection == '9':
        numwords = int(input("How many words to learn? " ))
        #words = readVocabFile()

        #each entry in pack is a string in format polish::english::right::wrong
        #These are actually removed from the files
        #when finished these will be appended to the correct files
        pack = generateRandomPack(numwords)
        print(pack)
        #print(pack)
        learning = True
        numcorrect = 0

    
        while learning:            
            print('\x1bc') #clear screen
            print("\n------------------------------------------")
            wordgroup = pack.pop(0)
            pol = wordgroup.split("::")[0]
            eng = wordgroup.split("::")[1]
            right = int(wordgroup.split("::")[2])
            wrong = int(wordgroup.split("::")[3])
            
            val = input(eng + " ... ")
            if val == 'q':
                learning = False
                newgroup = pol+"::"+eng+"::"+str(right)+"::"+str(wrong)+"::\n"
                pack.append(newgroup)
                break
            else:
                print(pol)
                val = input("Correct? (y)es / (n)o / (q)uit:  " )
                if val == 'y':
                    right += 1
                    numcorrect += 1
                    newgroup = pol+"::"+eng+"::"+str(right)+"::"+str(wrong)+"::\n"                    
                    pack.append(newgroup)
                elif val == 'n':
                    wrong += 1
                    numcorrect = 0 #reset
                    newgroup = pol+"::"+eng+"::"+str(right)+"::"+str(wrong)+"::\n"
                    pack.insert(math.ceil(numwords * .4), newgroup)
                elif val == 'q':
                    learning = False
                    newgroup = pol+"::"+eng+"::"+str(right)+"::"+str(wrong)+"::\n"
                    pack.append(newgroup)
                    break
                
            if numcorrect >= numwords:
                val = input("You got them all correct, would you like to continue? (y)es / (n)o / (q)uit:  " )
                if val == 'n' or val == 'q':
                    learning = False
                    
            print("\n")
            #words[index] = pol + "::" + eng + "::" + str(right) + "::" + str(wrong)

        #print(words)
        #for i in list(range(len(words))):
        #    words[i] += "\n"
            
        #with open("vocablist.txt", "w+") as file:
        #    file.writelines(words)
        writeVocabFile(vocab_temp, pack)
        fileWordsToFiles(pack)

        
    elif selection == '2':  #Add a new entry
        word_eng = input("English: " )
        word_pol = input("Polish: ")
        #Should check for duplicates in case word already exists
        with open(vocab_new, "r+", encoding='utf-8') as file:
            data = file.readlines()
        canadd = True
        for line in data:
            if line.split("::")[0] == word_pol:
                canadd = False
                break
            
        if canadd:
            f = open(vocab_new, "a+", encoding='utf-8')
            f.write(word_pol + "::" + word_eng + "::0::0::\n")
            f.close()


print("See ya next time!")
