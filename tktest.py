from tkinter import *
from wordgroup import WordGroup
from words import WordBag

class Example(Frame):
    def __init__(self, wordlist):
        super().__init__()
        #self.wordindex = 0
        self.english = True  #True for english and False for polish
        self.text = None
        self.wordbag = WordBag(wordlist)
        #self.wordlist = wordlist
        self.getNextWord()
        #self.current_word = self.getWord(self.wordindex)
        self.createUI()

    def createUI(self):
        #print(wordlist[0])
        self.master.title('Flash Card App')
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        label = Label(self, text="English", bg="white").grid(padx=10, pady=5, row=0, column=0, columnspan=3, sticky=W)
        self.text = Label(self, text=self.wordgroup.english, width=30, height=2, bg="yellow", font=("Helvetica", "20", "bold"))
        self.text.grid(padx=10, pady=5, row=1, column=0, columnspan=3, sticky=E+W+N+S)
        
        button = Button(self, text="Flip", command=self.flip).grid(row=2, column=1, sticky=E+W, padx=5, pady=5)
        button2 = Button(self, text="NO", command=self.nextcardNo).grid(row=3, column=0, sticky=E+W, padx=5, pady=5)
        button3 = Button(self, text="YES", command=self.nextcardYes).grid(row=3, column=2, sticky=E+W, padx=5, pady=5)
    
    def flip(self):
        '''Flip between english and polish'''
        self.english = not self.english
        self.displayWord()
        
    def nextcardYes(self):
        '''Get the next card in the list'''
        self.english = True
        self.wordgroup.incrementRight()
        self.wordbag.placeWord(self.wordgroup.raw, 100)
        self.getNextWord()
        self.displayWord()

    def nextcardNo(self):
        '''Get the next card in the list'''
        self.english = True
        self.wordgroup.incrementWrong()
        self.wordbag.placeWord(self.wordgroup.raw, 20)
        self.getNextWord()
        self.displayWord()

    def getNextWord(self):
        '''Get a word from the wordlist depending on the language set'''
        self.wordgroup = WordGroup(self.wordbag.getNextWord())

    def displayWord(self):
        '''Display either the english or polish version of the word'''
        if self.english:
            self.text.configure(text=self.wordgroup.english)
        else:
            self.text.configure(text=self.wordgroup.polish)


def main():
    root = Tk()
    #root.geometry("350x300+300+300")
    f = open("Vocab/vocab_new.txt", "r", encoding='utf-8')
    wordlist = []
    for line in f:
        wordlist.append(line.split('\n')[0])
    
    app = Example(wordlist)
    root.mainloop()


if __name__ == '__main__':
    main()
