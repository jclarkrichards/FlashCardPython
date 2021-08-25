import tkinter as tk
from tkinter import *
from tkinter import ttk
#from tkinter.ttk import *
from wordgroup import WordGroup
from words import WordBag
from files import Files
from random import randint

class FlashLearn(Frame):
    def __init__(self):
        super().__init__()
        self.english = True  #True for english and False for polish
        self.text = None
        self.masterval = None
        self.wordbag = None
     
        #self.masterlevel = 0
        self.radioChoiceVar = IntVar()
        self.packSizeVar = StringVar()
        self.setupUI()
        self.createTab1()
        self.createTab2()

        self.files = Files()
        self.seenwords = [] #What words have we already seen on our run?
        
        
             
    def setupUI(self):
        self.tabControl = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Set Up')
        self.tabControl.add(self.tab2, text='Learn')
        self.tabControl.pack(expand=1, fill='both')

    def createTab1(self):
        label1 = ttk.Label(self.tab1, text="Select learning style")
        label1.grid(row=0, column=0, padx=30, pady=30)
        r1 = Radiobutton(self.tab1, text="English - Polish", variable=self.radioChoiceVar, value=1)
        r1.grid(row = 1, column=0, sticky=W)
        r2 = Radiobutton(self.tab1, text="Polish - English", variable=self.radioChoiceVar, value=2)
        r2.grid(row = 2, column=0, sticky=W)
        r3 = Radiobutton(self.tab1, text="Random", variable=self.radioChoiceVar, value=3)
        r3.grid(row = 3, column=0, sticky=W)
        Button(self.tab1, text="Execute", command=self.makeWordPack).grid(row=4, column=0)

        label2 = ttk.Label(self.tab1, text="How many words in the pack?")
        label2.grid(row=0, column=1, padx=30, pady=30)
        entry1 = Entry(self.tab1, bd=5, textvariable=self.packSizeVar)
        entry1.grid(row=1, column=1)

    def createTab2(self):
        '''
        self.tab2.pack(fill=BOTH, expand=True)
        '''
        self.tab2.columnconfigure(0, weight=1)
        self.tab2.columnconfigure(1, weight=1)
        self.tab2.columnconfigure(2, weight=1)
        self.tab2.rowconfigure(0, weight=1)
        self.tab2.rowconfigure(1, weight=1)
        self.tab2.rowconfigure(2, weight=1)
        self.tab2.rowconfigure(3, weight=1)
        
        self.masterval = Label(self.tab2, text="0.0%", bg="white")
        self.masterval.grid(padx=10, pady=5, row=0, column=0, sticky=W)
        self.text = Label(self.tab2, text="Create a Pack", width=30, height=2, bg="yellow", font=("Helvetica", "20", "bold"))
        self.text.grid(padx=10, pady=5, row=1, column=0, columnspan=3, sticky=E+W+N+S)
        
        button = Button(self.tab2, text="Flip", command=self.flip).grid(row=2, column=1, sticky=E+W, padx=5, pady=5)
        button2 = Button(self.tab2, text="NO", command=self.nextcardNo).grid(row=3, column=0, sticky=E+W, padx=5, pady=5)
        button3 = Button(self.tab2, text="YES", command=self.nextcardYes).grid(row=3, column=2, sticky=E+W, padx=5, pady=5)

        buttonUpdate = Button(self.tab2, text="Start", command=self.startLearning).grid(row=0, column=1, sticky=E+W, padx=10, pady=10)

    def startLearning(self):
        #self.masterlevel = 0
        self.seenwords = []
        self.setWordCount()
        self.getNextWord()
        self.displayWord()

    def updateWordPack(self):
        '''Set the word pack to whatever is in temp.txt file.  This is a button in tab2'''
        f = open("Vocab/temp.txt", "r", encoding='utf-8')
        wordlist = []
        for line in f:
            wordlist.append(line.split('\n')[0])
        self.wordbag = WordBag(wordlist)
        #print(len(wordlist))
        #self.masterlevel = 0
        self.setWordCount()
        self.getNextWord()
        self.displayWord()

    def makeWordPack(self):
        '''Write to temp.txt file based off of the settings in tab1'''
        #print("Radio Selection = " + str(self.radioChoiceVar.get()))
        #print("Number of words to learn = " + self.packSizeVar.get())
        if self.wordbag is not None:
            self.files.fileWordsToFiles(self.wordbag.wordlist)
        radio_choice = int(self.radioChoiceVar.get())
        numwords = int(self.packSizeVar.get())
        #print(radio_choice, numwords)
        pack = self.files.generateRandomPack(numwords)
        self.wordbag = WordBag(pack)
        self.setStartLanguage()

    def setWordCount(self):
        '''To show how many words are in the pack, display in the upper right corner'''
        label = Label(self.tab2, text=str(len(self.wordbag.wordlist)))
        label.grid(padx=10, pady=5, row=0, column=2, sticky=E)
    
    def flip(self):
        '''Flip between english and polish'''
        self.english = not self.english
        self.displayWord()
        
    def nextcardYes(self):
        '''Get the next card in the list'''
        self.wordAlreadySeen(self.wordgroup.english)
        #self.masterlevel += 1
        self.setStartLanguage()
        last = self.wordgroup.last
        self.wordgroup.incrementRight()
        if last == 1: #got it right last time so place at end
            self.wordbag.placeWord(self.wordgroup.raw, 100)
        else:#Got it wrong last so place it in the middle
            self.wordbag.placeWord(self.wordgroup.raw, 50)
        self.getNextWord()
        self.displayWord()

    def nextcardNo(self):
        '''Get the next card in the list'''
        self.seenwords = []
        #self.masterlevel = 0
        self.setStartLanguage()
        last = self.wordgroup.last
        self.wordgroup.incrementWrong()
        if last == 0:  #got it wrong last time too, so see it more often
            self.wordbag.placeWord(self.wordgroup.raw, 15) 
        else:
            self.wordbag.placeWord(self.wordgroup.raw, 30)
        self.getNextWord()
        self.displayWord()

    def getNextWord(self):
        '''Get a word from the wordlist depending on the language set'''
        self.wordgroup = WordGroup(self.wordbag.getNextWord())

    def displayWord(self):
        '''Display either the english or polish version of the word'''
        #print(self.masterlevel)
        if self.english:
            self.text.configure(text=self.wordgroup.english)
        else:
            self.text.configure(text=self.wordgroup.polish)

        #print(self.wordbag.wordlist)
        val = len(self.seenwords) / len(self.wordbag.wordlist)
        #print(val)
        self.masterval.configure(text=str(abs(round(val, 2))))

        if val >= 1.0:
            print("Good job!.  You got them all right.  Go back and try some more!")
            self.masterval.configure(text="100%")
        else:
            self.masterval.configure(text=str(round(abs(val)*100))+"%")

    def setStartLanguage(self):
        '''The language to show when a new card is shown'''
        if int(self.radioChoiceVar.get()) == 1:
            self.english = True
        elif int(self.radioChoiceVar.get()) == 2:
            self.english = False
        else:
            rval = randint(0, 10)
            if rval < 5:
                self.english = True
            else:
                self.english = False

    def onClosing(self):
        '''When closing the window, save the words back into the vocab file'''
        #print("Window is closing, do something")
        if self.wordbag is not None:
            #self.files.returnTempToVocabFile()
            self.files.fileWordsToFiles(self.wordbag.wordlist)
        self.master.destroy()

    def wordAlreadySeen(self, word):
        '''Check to see if the word is already in the seenword list.  If not, then add it'''
        if word not in self.seenwords:
            self.seenwords.append(word)
        



def main():
    root = Tk()
    root.title("Flash Learn")
    root.geometry("500x350")
    app = FlashLearn()
    root.protocol("WM_DELETE_WINDOW", app.onClosing)
    root.mainloop()


if __name__ == '__main__':
    main()
